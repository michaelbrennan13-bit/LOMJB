"""Read-only Clio API v4 client for the Law Office of Michael J. Brennan, PLLC.

GET-only by design. Any attempt to write (POST/PUT/PATCH/DELETE) raises
`WriteAccessDisabled` — Clio write access (task creation, activity logging,
document upload) is a deliberately deferred v2 roadmap item. See ops/roadmap.md.

Endpoints and field names target Clio API v4 (https://app.clio.com/api/v4/).
Verify current endpoints/fields against https://docs.developers.clio.com if any
call 404s or a field is missing — Clio's schema evolves and the PI add-on data
lives in matter *custom fields*, which are account-specific.

Usage:
    from tools.clio.client import ClioClient
    clio = ClioClient()
    matters = clio.list_matters(fields="id,display_number,description,custom_field_values{...}")
    hits = clio.search_conflicts(["Acme Trucking LLC", "John Q. Defendant"])
"""

from __future__ import annotations

import time
from typing import Any, Iterable

import requests

from . import auth

API_BASE = "https://app.clio.com/api/v4"
_READ_ONLY_METHODS = {"GET", "HEAD"}


class WriteAccessDisabled(Exception):
    """Raised on any non-GET request. Write access is a v2 roadmap item."""


class ClioAPIError(Exception):
    """Raised when the Clio API returns an error response."""


class ClioClient:
    """Thin GET-only wrapper over the Clio API v4."""

    def __init__(self, base_url: str = API_BASE, timeout: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._session = requests.Session()

    # --- core request path -----------------------------------------------------
    def _headers(self) -> dict[str, str]:
        token = auth.get_valid_access_token()
        return {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }

    def _request(self, method: str, path: str, params: dict | None = None) -> dict:
        method = method.upper()
        if method not in _READ_ONLY_METHODS:
            raise WriteAccessDisabled(
                f"{method} is disabled. This client is read-only; Clio write access "
                "(task creation, activity logging, document upload) is a v2 roadmap "
                "item. See ops/roadmap.md."
            )

        url = path if path.startswith("http") else f"{self.base_url}/{path.lstrip('/')}"

        # One automatic retry on a 401, in case the token expired mid-session.
        for attempt in range(2):
            resp = self._session.request(
                method, url, headers=self._headers(), params=params, timeout=self.timeout
            )
            if resp.status_code == 401 and attempt == 0:
                # Force a refresh on the next _headers() call by nudging expiry.
                tokens = auth.load_tokens() or {}
                if tokens.get("refresh_token"):
                    auth.refresh_access_token(tokens["refresh_token"])
                    continue
            if resp.status_code == 429:  # rate limited — respect Retry-After once
                retry_after = float(resp.headers.get("Retry-After", "2"))
                time.sleep(min(retry_after, 10))
                continue
            if not resp.ok:
                raise ClioAPIError(
                    f"Clio API {method} {url} failed ({resp.status_code}): {resp.text[:500]}"
                )
            if not resp.content:
                return {}
            return resp.json()
        raise ClioAPIError(f"Clio API {method} {url} failed after retry.")

    def get(self, path: str, params: dict | None = None) -> dict:
        """Public GET. Explicitly guards against accidental write usage."""
        return self._request("GET", path, params=params)

    def _paginate(self, path: str, params: dict | None = None) -> Iterable[dict]:
        """Yield every record across Clio's paginated responses."""
        params = dict(params or {})
        params.setdefault("limit", 100)
        next_url: str | None = None
        while True:
            payload = self._request("GET", next_url or path, params=None if next_url else params)
            for record in payload.get("data", []):
                yield record
            paging = (payload.get("meta") or {}).get("paging") or {}
            next_url = paging.get("next")
            if not next_url:
                break

    # --- matters ---------------------------------------------------------------
    def list_matters(self, fields: str | None = None, **filters: Any) -> list[dict]:
        """List matters. Pass `fields` to include custom fields (PI add-on data).

        Example fields: "id,display_number,description,status,
        custom_field_values{id,field_name,value}"
        """
        params: dict[str, Any] = dict(filters)
        if fields:
            params["fields"] = fields
        return list(self._paginate("matters", params=params))

    def get_matter(self, matter_id: int | str, fields: str | None = None) -> dict:
        params = {"fields": fields} if fields else None
        return self._request("GET", f"matters/{matter_id}", params=params).get("data", {})

    # --- contacts --------------------------------------------------------------
    def list_contacts(self, fields: str | None = None, **filters: Any) -> list[dict]:
        params: dict[str, Any] = dict(filters)
        if fields:
            params["fields"] = fields
        return list(self._paginate("contacts", params=params))

    def search_contacts(self, query: str, fields: str | None = None) -> list[dict]:
        """Contacts matching a free-text query (Clio's `query` filter)."""
        params: dict[str, Any] = {"query": query}
        if fields:
            params["fields"] = fields
        return list(self._paginate("contacts", params=params))

    # --- calendar --------------------------------------------------------------
    def list_calendar_entries(self, fields: str | None = None, **filters: Any) -> list[dict]:
        params: dict[str, Any] = dict(filters)
        if fields:
            params["fields"] = fields
        return list(self._paginate("calendar_entries", params=params))

    # --- documents (metadata only) ---------------------------------------------
    def list_documents(self, fields: str | None = None, **filters: Any) -> list[dict]:
        """Document *metadata* only. This client never downloads or uploads content."""
        params: dict[str, Any] = dict(filters)
        if fields:
            params["fields"] = fields
        return list(self._paginate("documents", params=params))

    # --- activities ------------------------------------------------------------
    def list_activities(self, fields: str | None = None, **filters: Any) -> list[dict]:
        params: dict[str, Any] = dict(filters)
        if fields:
            params["fields"] = fields
        return list(self._paginate("activities", params=params))

    # --- conflict search -------------------------------------------------------
    def search_conflicts(self, names: list[str]) -> dict[str, dict[str, list[dict]]]:
        """Check each name against Clio contacts and matter participants.

        Returns a dict keyed by the searched name:
            {
              "Acme Trucking LLC": {
                 "contacts": [ {matching contact records} ],
                 "matters":  [ {matters whose display_number/description/client matched} ],
              },
              ...
            }

        Read-only. This surfaces *possible* hits for Michael's review; a clean
        result is not a complete conflict clearance (non-Clio relationships still
        require his judgment).
        """
        results: dict[str, dict[str, list[dict]]] = {}
        # Pull matters once with participant/client detail for local matching.
        matter_fields = (
            "id,display_number,description,"
            "client{id,name},"
            "matter_stage{name},"
            "relationships{id,contact{id,name}}"
        )
        try:
            all_matters = self.list_matters(fields=matter_fields)
        except ClioAPIError:
            # If the relationships/field expansion isn't supported on this account,
            # fall back to the minimal matter shape. Verify field names against
            # https://docs.developers.clio.com if this path is taken.
            all_matters = self.list_matters(
                fields="id,display_number,description,client{id,name}"
            )

        for name in names:
            needle = name.strip().lower()
            if not needle:
                continue

            contact_hits = self.search_contacts(
                name, fields="id,name,type,primary_email_address,primary_phone_number"
            )

            matter_hits: list[dict] = []
            for matter in all_matters:
                haystack_parts = [
                    str(matter.get("display_number", "")),
                    str(matter.get("description", "")),
                    str((matter.get("client") or {}).get("name", "")),
                ]
                for rel in matter.get("relationships", []) or []:
                    contact = rel.get("contact") or {}
                    haystack_parts.append(str(contact.get("name", "")))
                haystack = " | ".join(haystack_parts).lower()
                if needle in haystack:
                    matter_hits.append(matter)

            results[name] = {"contacts": contact_hits, "matters": matter_hits}
        return results


if __name__ == "__main__":
    # Smoke test: prove authorization works and the client is read-only.
    client = ClioClient()
    try:
        sample = client.list_matters(fields="id,display_number,description")[:3]
        print(f"OK — retrieved {len(sample)} sample matter(s).")
        for m in sample:
            print(f"  {m.get('display_number')}: {m.get('description')}")
    except Exception as exc:  # noqa: BLE001 - surface any setup error clearly
        print(f"Clio read failed: {exc}")
