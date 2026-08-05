"""Clio OAuth2 authorization-code flow and token management.

Read-only client for the Law Office of Michael J. Brennan, PLLC. Run this once
interactively to authorize:

    python tools/clio/auth.py

It opens the Clio consent screen, catches the redirect on a local port,
exchanges the code for tokens, and writes them to `.tokens.json` (gitignored).
After that, `client.py` refreshes the access token automatically as needed.

Credentials come from environment variables (see `.env.example`):
    CLIO_CLIENT_ID, CLIO_CLIENT_SECRET, CLIO_REDIRECT_URI

Standard library only (http.server, urllib, json, webbrowser) so there are no
runtime dependencies for auth itself. `client.py` uses `requests`.

NOTE: Clio's OAuth endpoints and API host can differ by region (US vs. EU/AU
shards). These defaults target the US shard (app.clio.com). If your Clio account
is on another shard, override the URLs below via environment variables. Verify
current endpoints against https://docs.developers.clio.com if anything fails.
"""

from __future__ import annotations

import json
import os
import time
import urllib.parse
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

# --- Endpoints (US shard defaults; override via env for other regions) ---------
AUTHORIZE_URL = os.environ.get("CLIO_AUTHORIZE_URL", "https://app.clio.com/oauth/authorize")
TOKEN_URL = os.environ.get("CLIO_TOKEN_URL", "https://app.clio.com/oauth/token")

# --- Local paths ---------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
TOKENS_PATH = _THIS_DIR / ".tokens.json"

# Default redirect target; must match the redirect URI registered in the Clio app.
DEFAULT_REDIRECT_URI = "http://127.0.0.1:8321/callback"


class ClioAuthError(Exception):
    """Raised when authorization or token exchange/refresh fails."""


def _client_id() -> str:
    value = os.environ.get("CLIO_CLIENT_ID")
    if not value:
        raise ClioAuthError("CLIO_CLIENT_ID is not set. Copy .env.example to .env and fill it in.")
    return value


def _client_secret() -> str:
    value = os.environ.get("CLIO_CLIENT_SECRET")
    if not value:
        raise ClioAuthError("CLIO_CLIENT_SECRET is not set. Copy .env.example to .env and fill it in.")
    return value


def _redirect_uri() -> str:
    return os.environ.get("CLIO_REDIRECT_URI", DEFAULT_REDIRECT_URI)


# --- Token persistence ---------------------------------------------------------
def load_tokens() -> dict | None:
    """Return the stored token bundle, or None if not authorized yet."""
    if not TOKENS_PATH.exists():
        return None
    with TOKENS_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save_tokens(tokens: dict) -> None:
    """Persist tokens to .tokens.json, stamping an absolute expiry time."""
    if "expires_in" in tokens and "expires_at" not in tokens:
        # Record an absolute expiry with a small safety margin.
        tokens["expires_at"] = time.time() + float(tokens["expires_in"]) - 60
    with TOKENS_PATH.open("w", encoding="utf-8") as fh:
        json.dump(tokens, fh, indent=2)
    # Tokens are secrets; keep them owner-only.
    try:
        TOKENS_PATH.chmod(0o600)
    except OSError:
        pass


# --- OAuth flow ----------------------------------------------------------------
def _build_authorize_url(state: str) -> str:
    params = {
        "response_type": "code",
        "client_id": _client_id(),
        "redirect_uri": _redirect_uri(),
        "state": state,
    }
    return f"{AUTHORIZE_URL}?{urllib.parse.urlencode(params)}"


def _exchange_code_for_tokens(code: str) -> dict:
    data = urllib.parse.urlencode(
        {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": _client_id(),
            "client_secret": _client_secret(),
            "redirect_uri": _redirect_uri(),
        }
    ).encode("utf-8")
    req = urllib.request.Request(TOKEN_URL, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:  # pragma: no cover - network error path
        body = exc.read().decode("utf-8", errors="replace")
        raise ClioAuthError(f"Token exchange failed ({exc.code}): {body}") from exc


def refresh_access_token(refresh_token: str) -> dict:
    """Exchange a refresh token for a new access token bundle."""
    data = urllib.parse.urlencode(
        {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": _client_id(),
            "client_secret": _client_secret(),
        }
    ).encode("utf-8")
    req = urllib.request.Request(TOKEN_URL, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    try:
        with urllib.request.urlopen(req) as resp:
            tokens = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:  # pragma: no cover - network error path
        body = exc.read().decode("utf-8", errors="replace")
        raise ClioAuthError(f"Token refresh failed ({exc.code}): {body}") from exc

    # Clio may not return a new refresh token on every refresh; keep the old one.
    if "refresh_token" not in tokens:
        tokens["refresh_token"] = refresh_token
    save_tokens(tokens)
    return tokens


def get_valid_access_token() -> str:
    """Return a live access token, refreshing or prompting for authorization as needed.

    Called by client.py before every request.
    """
    tokens = load_tokens()
    if not tokens:
        raise ClioAuthError(
            "Not authorized yet. Run `python tools/clio/auth.py` once to authorize."
        )

    expires_at = tokens.get("expires_at", 0)
    if time.time() >= expires_at:
        refresh_token = tokens.get("refresh_token")
        if not refresh_token:
            raise ClioAuthError(
                "Access token expired and no refresh token on file. "
                "Re-run `python tools/clio/auth.py`."
            )
        tokens = refresh_access_token(refresh_token)

    access_token = tokens.get("access_token")
    if not access_token:
        raise ClioAuthError("No access token on file. Re-run `python tools/clio/auth.py`.")
    return access_token


# --- Local redirect catcher ----------------------------------------------------
class _CallbackHandler(BaseHTTPRequestHandler):
    """One-shot handler that captures the ?code=... from Clio's redirect."""

    server_version = "AugustClioAuth/1.0"
    captured: dict = {}

    def do_GET(self) -> None:  # noqa: N802 - required signature
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path != urllib.parse.urlparse(_redirect_uri()).path:
            self.send_response(404)
            self.end_headers()
            return
        params = urllib.parse.parse_qs(parsed.query)
        _CallbackHandler.captured = {k: v[0] for k, v in params.items()}
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(
            b"<html><body><h2>August is authorized with Clio.</h2>"
            b"<p>You can close this tab and return to the terminal.</p></body></html>"
        )

    def log_message(self, *args) -> None:  # noqa: D401 - silence default logging
        return


def authorize_interactive() -> dict:
    """Run the full authorization-code flow. Returns the saved token bundle."""
    redirect = urllib.parse.urlparse(_redirect_uri())
    host = redirect.hostname or "127.0.0.1"
    port = redirect.port or 8321

    state = os.urandom(16).hex()
    auth_url = _build_authorize_url(state)

    print("Opening the Clio consent screen in your browser...")
    print(f"If it doesn't open, paste this URL:\n\n{auth_url}\n")
    try:
        webbrowser.open(auth_url)
    except Exception:  # pragma: no cover - headless environments
        pass

    httpd = HTTPServer((host, port), _CallbackHandler)
    print(f"Waiting for the redirect on {host}:{port} ...")
    # Serve requests until we capture a code (or an error) on the callback path.
    while not _CallbackHandler.captured:
        httpd.handle_request()
    httpd.server_close()

    captured = _CallbackHandler.captured
    if "error" in captured:
        raise ClioAuthError(f"Authorization denied: {captured.get('error')}")
    if captured.get("state") != state:
        raise ClioAuthError("State mismatch — possible CSRF. Aborting.")
    code = captured.get("code")
    if not code:
        raise ClioAuthError("No authorization code returned.")

    tokens = _exchange_code_for_tokens(code)
    save_tokens(tokens)
    print(f"Authorized. Tokens saved to {TOKENS_PATH}")
    return tokens


if __name__ == "__main__":
    authorize_interactive()
