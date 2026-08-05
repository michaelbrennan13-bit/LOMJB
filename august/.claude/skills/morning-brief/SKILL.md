---
name: morning-brief
description: Produce Michael's morning brief — today's calendar with prep notes, top emails needing action with draft replies, deadlines and court dates inside 14 days, and drafts awaiting his approval. Use when Michael says "brief me," "morning brief," "what's my day," or "catch me up." Also the entry point for the scheduled weekday run.
---

# Morning Brief

The daily orientation. Runs manually ("brief me") or as the scheduled weekday run (`ops/scheduled/morning-brief.md`). **Bottom line first, under a page.** Read-only scan; drafts only, nothing sent.

## Sources

- **Outlook** — mail + calendar (primary).
- **Gmail** — personal, triage-scan only.
- Open **drafts** in `matters/*/drafts/` and Outlook drafts awaiting approval.

## Workflow

1. **Calendar today.** Pull today's Outlook calendar. For each event, a one-line prep note (what it is, what Michael needs in hand). Apply the `calendar` skill's court-setting travel padding — flag any in-person court appearance and whether travel time is blocked.
2. **Top emails needing action.** Run the `email-triage` logic and surface the **top 5** items needing action, each with a one-line summary and a **draft reply queued** (Tier 2 — drafted, not sent). Priority senders (courts, opposing counsel, adjusters) always make the list.
3. **Deadlines & court dates inside 14 days.** Anything you can see — from Clio calendar entries, court notices in email, matter `context.md` key dates — with a hard or soft deadline in the next 14 days. Mark each with its source and a `[VERIFY]` where the date is computed rather than confirmed. (This is a *visibility* scan, not the v2 deadline register — say so if coverage is partial.)
4. **Open drafts awaiting approval.** List every draft sitting in `matters/*/drafts/` or Outlook drafts that's waiting on Michael, with its matter and what it's for.

## Output format

```
# Morning Brief — <Weekday, Month D, YYYY>

**Bottom line:** <the 1–2 things that actually matter today>

## Today
- <time> — <event> — <one-line prep note> [travel blocked / FLAG conflict]
...

## Needs action (top 5)
1. <sender> — <one line> — [reply drafted, awaiting send]
...

## Deadlines & court dates — next 14 days
- <date> — <matter> — <what> — <source> [VERIFY if computed]
...

## Drafts awaiting your approval
- <matter> — <doc> — <what it's for>
...
```

Keep it **under a page.** If a section is empty, say "none" in one line and move on. If something is on fire, it goes in the bottom line, not buried in a list.

## Tiers

Everything here is Tier 1 (reading, scanning, drafting) except the queued replies, which are Tier 2 (drafted, never sent). Say so where relevant; don't send anything.
