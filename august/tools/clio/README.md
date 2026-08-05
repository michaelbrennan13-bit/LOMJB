# Clio Integration (read-only)

A GET-only client for Clio Manage API v4. August uses it to pull matters (with PI add-on custom fields), contacts, calendar entries, document metadata, and activities — and to run conflict checks. It **cannot write** anything to Clio; write access is a v2 roadmap item.

## One-time setup (Michael)

### 1. Create a Clio developer app

1. Go to the **Clio Developer Portal** (from your Clio account: Settings → **Developer** / App integrations, or the developer portal at [developers.clio.com](https://developers.clio.com)).
2. Create a new application.
3. Set the **Redirect URI** to exactly:

   ```
   http://127.0.0.1:8321/callback
   ```

4. Request read scopes for matters, contacts, calendar, documents, and activities.
5. Copy the **Client ID** and **Client Secret**.

### 2. Put credentials in `.env`

From the repo root:

```bash
cp .env.example .env
```

Then edit `.env` and fill in:

```
CLIO_CLIENT_ID=...
CLIO_CLIENT_SECRET=...
CLIO_REDIRECT_URI=http://127.0.0.1:8321/callback
```

`.env` and `.tokens.json` are gitignored — they never sync to GitHub.

### 3. Authorize once

Make sure the env vars are loaded, then run:

```bash
python tools/clio/auth.py
```

This opens the Clio consent screen, catches the redirect locally, and writes tokens to `tools/clio/.tokens.json`. After this, the access token refreshes automatically — you shouldn't need to run it again unless the refresh token is revoked.

### 4. Verify it works

```bash
python -m tools.clio.client
```

Prints a few sample matters if authorization succeeded.

> Loading `.env`: the auth flow reads plain environment variables. Export them in your shell, use a tool like `direnv`, or `set -a; source .env; set +a` before running.

## Endpoints & fields — verify at build time

Clio API v4 lives at `https://app.clio.com/api/v4/`. Endpoint paths and field names evolve, and the **PI add-on data lives in matter custom fields** that are specific to your account. If a call 404s or a field is missing:

- Check current docs at **[docs.developers.clio.com](https://docs.developers.clio.com)**.
- Confirm your account's **shard** (US `app.clio.com` vs. EU/AU). Override endpoints via `CLIO_AUTHORIZE_URL`, `CLIO_TOKEN_URL`, and the client `base_url` if you're not on the US shard.
- List a matter with `fields=custom_field_values{id,field_name,value}` to see your account's actual PI field names.

## Files

| File | What it does |
|---|---|
| `auth.py` | OAuth2 authorization-code flow, local redirect catch, token persistence + auto-refresh. Stdlib only. |
| `client.py` | GET-only wrapper: `list_matters`, `get_matter`, `list_contacts`, `search_contacts`, `list_calendar_entries`, `list_documents`, `list_activities`, `search_conflicts`. Hard-fails any non-GET method. Uses `requests`. |
| `.tokens.json` | Created on first authorize. Gitignored. Owner-readable only. |

## Read-only guarantee

`client.py` raises `WriteAccessDisabled` on any POST/PUT/PATCH/DELETE. This is intentional: August prepares and reads, she does not mutate the system of record. Write access (task creation, activity logging, document upload) is item 5 on `ops/roadmap.md`.
