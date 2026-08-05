---
name: demand-letter
description: Draft a plaintiff-side settlement demand letter for a personal injury matter. Use when Michael says "draft a demand," "write a demand letter," "demand for <matter>," or asks to demand policy limits or make a Stowers demand. Reads matter context or works from pasted facts, builds the liability narrative, injuries, medical specials table, damages, and demand figure with deadline.
---

# Demand Letter

Draft a settlement demand letter in the firm's plain-English demand register (`firm/voice.md`, Register 1).

## Input

One of:
- A **matter slug** — read `matters/<slug>/context.md` and `matters/<slug>/contacts.md`. If context is thin or missing, run the `matter-context` skill first to build it.
- **Facts pasted directly** into the conversation.

If you have a slug but no context file yet, say so and offer to build it before drafting.

## Workflow

Build the letter in this order. Each section flows into the next; the reader should finish knowing what happened, how badly the client was hurt, what it cost, and what you want.

1. **Opening — the demand, stated first.** Per voice: the demand figure and the deadline go in the opening paragraph. No throat-clearing. Identify the client, the incident date, and that this is a settlement demand. Example shape: *"This firm represents [client] for injuries suffered in the [date] collision your insured caused. We demand [$figure] to settle all claims. This offer is open until [date]."*

2. **Liability narrative.** What happened, in plain English and short sentences. Establish the defendant's negligence and causation. Pull specific facts — the police report, the citation, the ELD data, the scene. Mark every factual assertion you cannot see in the record as needing confirmation. Cite the duty/standard where it sharpens the point (e.g., FMCSA hours-of-service for trucking) with a `[VERIFY]` marker unless you fetched it.

3. **Injuries and treatment.** The medical story chronologically: mechanism of injury, initial complaints, diagnostic findings, course of treatment, procedures, current status, and prognosis. Tie injuries to the collision. Flag any causation gap or pre-existing condition Michael should be ready for.

4. **Medical specials table.** A clean table of billed charges:

   | Provider | Dates of service | Description | Billed |
   |---|---|---|---|
   | ... | ... | ... | $... |
   | | | **Total billed** | **$...** |

   Use only figures grounded in records/bills in the file. Where a bill is missing, list the provider and mark the amount `[VERIFY — bill not in file]`. Note if you're using billed vs. paid/adjusted and flag the Texas paid-or-incurred limitation (**CPRC § 41.0105 `[VERIFY]`**) for Michael's call on which figure to present.

5. **General damages.** Pain, suffering, mental anguish, physical impairment, disfigurement, loss of enjoyment — grounded in the specific facts of this injury and recovery, not boilerplate. Where lost wages / loss of earning capacity apply, state the basis and mark unverified figures.

6. **Demand figure and deadline.** Restate the number and the deadline. State what the number covers (all claims, full and final) and that acceptance requires a release. Keep the deadline reasonable and concrete (a date, not "30 days").

## Stowers awareness

When **policy limits are known** and **liability is reasonably clear**, structure the letter to qualify as a **Stowers demand** so it sets up the insurer's duty to settle within limits. Include and check off the elements:

- [ ] A clear, unconditional offer to settle **within policy limits**
- [ ] For a full release of the insured
- [ ] A **reasonable deadline** to accept
- [ ] Terms an ordinarily prudent insurer would accept
- [ ] Liability reasonably clear and damages exceeding limits

Put this checklist in the draft as a note to Michael, marked **`[VERIFY against current Stowers line of cases]`** (*Stowers Furniture v. American Indemnity* and its progeny — confirm current elements and any recent Texas Supreme Court refinements). Do not assert the letter *is* a valid Stowers demand; present the elements and let Michael confirm.

If limits are unknown, add a policy-limits demand/request and note that Stowers structure kicks in once limits are confirmed.

## Citations and confidentiality

- Every legal citation carries `[VERIFIED — source]` or `[VERIFY — what/where]`. Fetch Texas statutes from `statutes.capitol.texas.gov` and upgrade to VERIFIED when you read them.
- Client facts stay in the file. Any legal research to support the demand uses genericized queries.

## Ethics screen

Run the letter past `firm/ethics.md`. A demand is not promotional, but confirm no fee or confidentiality issue, and that the release/settlement terms don't stray into Tier 3 (you draft; you never communicate acceptance or authority).

## Output

- Write to `matters/<slug>/drafts/`.
- Filename: `demand-<yyyy-mm-dd>.docx` (or `.md`).
- Prefer **`.docx` via the `docx` skill** when available so it's on letterhead and ready for review; fall back to `.md` otherwise.
- This is a **draft** (Tier 1). It is not sent. Sending is Tier 2 and Michael's call.

## Close

End your turn to Michael with:
1. The one-line bottom line (who, how much, deadline).
2. Any `[VERIFY]` flags that need his attention before it goes out.
3. The question: **"Generalize this into a template in `templates/`?"** — if yes, strip the client-specific facts and save a reusable skeleton per `templates/README.md`.
