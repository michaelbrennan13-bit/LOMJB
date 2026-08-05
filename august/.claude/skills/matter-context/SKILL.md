---
name: matter-context
description: Build or refresh a matter's context.md by pulling from Clio, OneDrive/SharePoint, and email. Use when Michael says "open a matter for," "build context on <matter>," "refresh <matter>," "catch me up on <case>," or when another skill needs matter context that's missing or stale. This is the skill other skills call first.
---

# Matter Context

Assemble everything known about a matter into `matters/<slug>/context.md` so every other skill can read it first. Read-only across all sources.

## Input

A matter slug (`lastname-yyyy-shortdesc`) or a Clio matter reference. If the matter folder doesn't exist yet, create it from `matters/_TEMPLATE/`.

## Sources — pull from all three, read-only

1. **Clio** via `tools/clio/client.py` (GET-only):
   - Matter record + **custom fields** (the PI add-on data — injuries, coverage, adjuster, policy limits live here).
   - Contacts / matter participants → feeds `contacts.md`.
   - Calendar entries tied to the matter → key dates.
   - Documents metadata and activities → what exists and what's happened.
2. **OneDrive / SharePoint:** search the matter's document folder — pleadings, correspondence, records, bills.
3. **Email:** search Outlook (and Gmail if relevant) for the matter — recent correspondence with client, adjuster, opposing counsel, providers.

## Workflow

1. Create/locate `matters/<slug>/`. If new, copy `_TEMPLATE/` structure (`context.md`, `contacts.md`, `drafts/`).
2. Pull from all three sources above.
3. Populate `context.md`:

```
# Matter: <slug>
Client: <name>   |   Matter type: <trucking / MVC / premises / ...>   |   Status: <posture>
Clio matter ID: <id>   |   Last refreshed: <yyyy-mm-dd>

## Parties
- Plaintiff/client: ...
- Defendant(s) and related entities: ...
- Insurers / adjusters: ...
- Opposing counsel: ...

## Facts
<what happened — date, location, mechanism, plain English>

## Injuries & treatment
<injuries, providers, procedures, current status, prognosis>

## Coverage
<policies, limits where known, UM/UIM, source of each figure>

## Posture
<where the matter stands: pre-suit / suit filed / discovery / demand out / etc.>

## Key dates
<incident date; limitations bar date [VERIFY — CPRC § 16.003]; court settings;
 deadlines; demand deadlines. Mark each source (Clio calendar / court notice / computed).>

## Open items
<what's missing, what's next, what needs Michael>
```

4. Populate `contacts.md` from Clio contacts + email signatures (client, adjusters with claim numbers, opposing counsel, providers, lienholders).
5. Note the `Last refreshed` date. On a refresh, update in place and note what changed.

## Rules

- **Read-only everywhere.** No writes to Clio, SharePoint, or email. Building the local `context.md` is a Tier 1 memory update.
- **Citation discipline** applies to any legal date you compute: limitations and deadlines carry `[VERIFY]` markers and note how you derived them. Deadline *tracking as a system* is a v2 roadmap item — here you record what you can see, you don't build a deadline register.
- Real client names and facts belong in these files (confidential repo). Don't anonymize.

## Output

`matters/<slug>/context.md` and `contacts.md`, written/refreshed. Report to Michael: the one-line posture, the limitations bar date, and the top open items.
