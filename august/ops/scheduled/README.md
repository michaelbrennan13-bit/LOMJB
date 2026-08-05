# Scheduled Runs

How to wire August's recurring runs. The morning brief is the one built for v1; `morning-brief.md` in this folder is the complete, standalone prompt a scheduled session feeds her.

## What runs

`ops/scheduled/morning-brief.md` — a self-contained prompt that tells a fresh session to load this repo, become August per `CLAUDE.md`, run the `morning-brief` skill, and deliver the brief. It's locked to read-only + drafts-only, so it's safe to run unattended.

## Wiring option A — Cowork scheduled task (recommended)

This is the route that works **when the laptop is closed**, because it runs in the cloud against the GitHub repo.

1. Push this repo to GitHub (see the root `README.md` first-run checklist).
2. In a Cowork session pointed at this repo, ask it to schedule a recurring task:
   > "Schedule a task every weekday at 7:00 a.m. Central that runs the prompt in `ops/scheduled/morning-brief.md` against this repo."
3. Confirm the schedule (weekdays, 07:00 America/Chicago) and that the connectors August needs — **Microsoft 365** and **Gmail** — are attached to the scheduled run so she can reach mail and calendar.

The scheduled session becomes August, runs the brief, and delivers it. Because it's cloud-side, it doesn't depend on the Mac being awake.

## Wiring option B — local cron (Mac, headless Claude Code)

Runs on the Mac; only fires when the machine is awake and online. Use it as a fallback or if you prefer local.

```cron
# Morning brief, weekdays at 7:00 a.m. (server local time — set the Mac to Central)
0 7 * * 1-5  cd /path/to/august && /usr/local/bin/claude -p "$(cat ops/scheduled/morning-brief.md)" >> ops/scheduled/last-run.log 2>&1
```

- Replace `/path/to/august` with the repo path and confirm the `claude` binary path (`which claude`).
- The Mac must be awake at 7:00 a.m. — the Cowork route (Option A) is the one that survives a closed laptop.
- Ensure the M365 and Gmail connectors are authorized for the local Claude Code environment.

## Notes

- Both routes run the **same** `morning-brief.md`, so the brief is identical wherever it fires.
- The run is read-only and drafts-only by design — nothing it does needs approval-gating beyond the tiers already baked into the prompt.
- To change the schedule or add a second scheduled skill later (e.g., a weekly deadline sweep once the v2 register ships), add another prompt file here and wire it the same way.
