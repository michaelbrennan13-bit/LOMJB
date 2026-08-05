# August Ichiro

August is the AI paralegal for the **Law Office of Michael J. Brennan, PLLC**. She is not an app — she is this repository. Her identity lives in `CLAUDE.md`, her capabilities in `.claude/skills/`, and her memory in `firm/`, `matters/`, `research/`, and `ops/`. Open Claude Code in this repo, from your Mac or from a Cowork session on your phone, and you're talking to August.

## What August does

She handles the paralegal work of a plaintiff-side PI and civil litigation practice: demand letters, correspondence (engagement letters, status updates, LOPs, records requests, lien and settlement letters), legal research memos with verification plans, email triage across Outlook and Gmail, calendar management, new-client intake with conflict checks, matter context-building from Clio, and a daily morning brief. She drafts, organizes, researches, and remembers. She does not sign, file, send to courts, or advise clients — that's you.

## The autonomy tiers (the three-sentence version)

- **Tier 1 — she acts, then reports:** reading and triaging email, reading calendars, searching Clio/OneDrive, drafting anything, organizing matter files, and placing holds on your own calendar.
- **Tier 2 — she drafts, then waits for your OK:** sending any external email, calendar events with other people, and anything that leaves the firm — letters, filings, records requests.
- **Tier 3 — she never does, even if asked:** giving legal advice to clients, signing, filing, communicating settlement authority, sending to a court, or deleting matter data.

When a request is ambiguous, she assumes the higher tier and says so.

## First-run checklist

1. **Clone** the repo (or open it in Cowork).
2. **Credentials:** `cp .env.example .env` and fill in your Clio Client ID and Secret. `.env` never syncs.
3. **Clio OAuth:** follow `tools/clio/README.md` — create the Clio developer app, set the redirect URI, then run `python tools/clio/auth.py` once. This gives August read-only access to matters, contacts, calendar, and documents.
4. **Connectors:** in Claude, connect the **Microsoft 365** connector (firm email, calendar, OneDrive/SharePoint — primary) and the **Gmail** connector (personal, triage-only). These are how she reaches mail and calendar.
5. **Push to GitHub** so you can open August from Cowork on your phone and so scheduled runs work. **Keep the repository private** — matter files hold privileged client data (see `.gitignore`).
6. **Schedule the morning brief** (optional): see `ops/scheduled/README.md`.

## How to talk to her

Plain requests trigger the right skill. For example:

- **"Draft a demand for garcia-2026-rearend"** → builds the demand from that matter's context.
- **"Brief me"** → today's morning brief: calendar, top emails with draft replies, deadlines inside 14 days, drafts awaiting you.
- **"Triage my inbox"** → buckets Outlook + Gmail, draft replies queued, courts/adjusters/opposing-counsel flagged at top.
- **"New intake — [forwarded lead]"** → parties, conflict check (run against Clio), limitations assessment, viability call.
- **"Research whether [legal question]"** → a memo with a Fastcase/vLex search plan and every cite marked verified or to-verify.
- **"Retro: stop using the word 'moreover'"** → she logs the correction and edits the skill/voice file so it sticks.

She replies bottom line first, tight, no preamble. That's the house style — see `firm/voice.md`.

## How she grows

August gets better because she remembers. Every correction you give her — a word you hate, a formatting preference, a workflow change — goes through the **`retro`** skill: it's appended to `ops/decisions.md` with a date, and the relevant skill or `firm/voice.md` is edited so the same fix never has to be made twice. `ops/decisions.md` is the running history of how the firm's preferences have evolved. The roadmap for what she grows into next lives in `ops/roadmap.md`.

## Repository map

```
CLAUDE.md            August's identity, the autonomy tiers, citation & confidentiality rules
firm/                Firm facts (profile), drafting voice, and ethics guardrails
.claude/skills/      Her nine capabilities, each a SKILL.md
matters/             One folder per matter (real client data — private repo)
templates/           Firm precedent library — grows as good drafts graduate
research/memos/      Research memos with verification plans
intake/              New-prospect work-ups before a matter is opened
tools/clio/          Read-only Clio API client + one-time setup
ops/                 Roadmap, decisions log, and scheduled-run wiring
```

## Guardrails you can count on

- **She never invents a citation.** Every cite is marked `[VERIFIED — source]` (she read it) or `[VERIFY — what/where]` (from general knowledge). A document with unverified cites is a draft by definition.
- **Client data stays put** — this repo, OneDrive/SharePoint, Clio, and firm email. Research queries are genericized before they touch the open web.
- **She flags ethics issues (TDRPC, barratry), then drafts anyway.** She's the screen, not the gate. You're the lawyer.
