# Roadmap — v2 and beyond

What August grows into next, in priority order. v1 is the scaffold you're reading. Each item below is deferred on purpose — noted where the deferral is a safety decision, not just scope.

## 1. Deadline & SOL register (per matter)
A real deadline system: statute-of-limitations dates (CPRC limitations), TRCP deadlines, discovery cutoffs, court-set deadlines, and warning windows that surface before they hit. **Deliberately deferred from v1** — a half-built deadline system is more dangerous than none, because it invites reliance it can't yet earn. Until this ships, August *surfaces* dates she can see (in the morning brief and matter context) with `[VERIFY]` markers, and never presents deadline coverage as complete.

## 2. Medical records chronologies & specials summaries
Turn records and bills into a clean treatment chronology and a specials summary that feeds directly into the `demand-letter` skill's injuries section and specials table — so the demand builds from structured data, not manual re-entry.

## 3. Discovery skill
Interrogatories, requests for production, requests for admission, and responses/objections — Texas-form, with objection libraries and the plain-English/formal register split.

## 4. Pleadings & motions skill
Petitions, motions, and orders with correct **Fort Bend / Harris County local-rule formatting**, captions, and certificates. Pairs with the Tier 3 line: August drafts; Michael signs and files.

## 5. Clio write access
Task creation, activity/time logging, and document upload — lifting the read-only limit in `tools/clio/`. Gated behind careful tier design so writes to the system of record stay controlled.

## 6. Browser automation for Fastcase / vLex
Semi-automate research verification so the `research-memo` search plans can be run against the State Bar member-benefit databases (which have no API) instead of handed to Michael to run manually.

## 7. Estate-planning document suite
Wills, powers of attorney, medical directives, and related instruments — Texas Estates Code forms, in the formal register.

## 8. Intake wired to the website
Connect `intake` directly to the **mjbrennan.com** Web3Forms endpoint so inbound web inquiries flow into the intake pipeline automatically (inbound only — barratry line holds).
