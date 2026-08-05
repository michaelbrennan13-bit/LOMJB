---
name: intake
description: Work up a new prospect from a web form, call notes, or a forwarded email into an intake summary — parties, facts, conflict check, limitations assessment, and case-viability first pass. Use when Michael forwards a new lead, says "new intake," "work up this prospect," "run a conflict check on," or "should we take <case>." Runs the Clio conflict search read-only; drafts an engagement letter only if Michael says take it.
---

# Intake

Turn an inbound inquiry into a decision-ready intake package. **Inbound only** — the firm responds to inquiries; it never drafts outbound solicitation to accident victims (barratry — see below).

## Input

A web form submission, call notes, or a forwarded email from a prospect. Extract everything; don't make the prospect's facts up where the input is thin — flag gaps.

## Workflow — produce all five

### 1. Parties and facts summary
- Prospect (name, contact, role — injured party, family, etc.).
- Adverse parties and every related entity you can identify (driver, employer/motor carrier, vehicle owner, premises owner/manager, contractor chain, insurers).
- What happened: date, location, mechanism, injuries claimed, treatment so far, current status.
- Plain-English narrative, short. Flag missing facts.

### 2. Conflict-check list — and run it
- List **every adverse party and related entity** to check.
- **Run the search yourself, read-only**, via `tools/clio/client.py` → `search_conflicts([names])`, which checks Clio contacts and matter participants.
- **Report hits** with the matching contact/matter, or state clearly "no conflicts found in Clio" — and note that a clean Clio search is not a complete conflict clearance (Michael's judgment on non-Clio relationships still applies).

### 3. Limitations assessment
- Presumptive **two-year limitations for personal injury** — **Tex. Civ. Prac. & Rem. Code § 16.003 `[VERIFY]`**.
- State the **accrual date** (usually the incident date) and compute the presumptive bar date.
- Flag **tolling / accrual questions**: discovery rule, minor or incapacitated claimant, governmental defendant (**Texas Tort Claims Act notice deadlines — much shorter, `[VERIFY]`**), wrongful death vs. survival accrual, any date ambiguity.
- If the bar date is close or uncertain, say so loudly at the top — this is the expensive miss.

### 4. Case-viability first pass
- **Liability theory:** the negligence/duty theory and how clear fault looks.
- **Coverage prospects:** likely insurance (auto limits, commercial/motor-carrier policies, premises GL, UM/UIM), and whether limits will cover the damages.
- **Damages signal:** injury severity, treatment trajectory, specials so far, general-damages picture.
- Bottom line: a ranked take — **take / decline / need-more-info** — with your one-sentence reason.

### 5. Draft engagement letter — only if Michael says take it
- Do **not** draft it on your own initiative. When Michael says take the case, hand off to the `correspondence` skill's engagement-letter flow (contingency-fee requirements flagged — **Tex. Gov't Code § 82.065 `[VERIFY]`**, TDRPC 1.04).

## Barratry note

**Tex. Penal Code § 38.12 `[VERIFY current text]`.** Intake responds to **inbound** inquiries only. You never draft outbound solicitation to accident victims or their families. If an inquiry looks like it originated from improper solicitation, flag it for Michael before proceeding.

## Confidentiality

Prospect facts stay in this repo and Clio. Any research (e.g., checking a defendant entity) uses genericized queries and public sources only.

## Output

- Write the intake package to `intake/<lastname>-<yyyy-mm-dd>.md`.
- This lands in `intake/` — it becomes a matter only when Michael takes it (then `matter-context` opens `matters/<slug>/`).
- Report to Michael bottom line first: **take/decline/need-more**, limitations bar date, conflict result, and coverage read — in the first four lines.
