---
name: correspondence
description: Draft firm letters and client-facing documents — engagement letters, status updates, letters of protection, medical records requests, lien negotiation letters, and closing/settlement statements. Use when Michael says "draft an engagement letter," "send a status update to <client>," "records request to <provider>," "LOP," "lien letter," or "settlement statement."
---

# Correspondence

Draft firm letters in the plain-English register (`firm/voice.md`, Register 1). Point or ask stated first, short sentences, no "please be advised."

## Input

A matter slug (read `matters/<slug>/context.md` and `contacts.md`) or facts pasted directly. Confirm the recipient and the exact ask before drafting.

## Document types

### Engagement letter
Scope of representation, the specific matter, contingency fee structure, expenses/costs handling, client and firm responsibilities, termination, and file-retention terms.
- **Flag the contingency-fee requirements:** must be in writing and signed — **Tex. Gov't Code § 82.065 `[VERIFY]`** — and reasonable under **TDRPC 1.04 `[VERIFY]`**. Put the flag at the top.
- If the matter came through the allied firm, add the fee-sharing terms and flag **TDRPC 1.04(f) `[VERIFY]`** (written client consent, proportionality, total fee reasonable).

### Status update
Where the matter stands, what's happened since last contact, what's next, and what (if anything) you need from the client. Plain English, no legalese, reassuring but not promising outcomes. Never state legal advice — report status; Michael advises.

### Letter of protection (LOP)
To a provider, protecting their bill from settlement proceeds so the client can treat. State the matter, the firm's undertaking to protect the balance from any recovery, and the limits of that undertaking. Flag that an LOP is a firm obligation Michael must approve — Tier 2 to send.

### Medical records request
To a provider, requesting complete records and itemized bills for the client's treatment.
- Include **HIPAA-compliant authorization** language and reference the signed authorization. Mark the authorization/statutory language **`[VERIFY — current HIPAA authorization elements and any Texas medical-records-request statute/fee limits]`**.
- Specify date range, records + billing, and the format/delivery you want.

### Lien negotiation letter
To a lienholder (hospital, health plan, Medicare/Medicaid, statutory lien claimant), requesting reduction. State the recovery constraints, the equities, and the specific reduction requested. Flag the governing lien framework (**Texas hospital lien — Tex. Prop. Code ch. 55 `[VERIFY]`**; ERISA plan / Medicare Secondary Payer where applicable `[VERIFY]`) so Michael knows which rules bind the negotiation.

### Closing / settlement statement
The disbursement breakdown for the client: gross settlement, attorney's fee, case expenses itemized, medical liens/balances, net to client. Must reconcile to the penny. Flag that funds move through the **Esquire Bank IOLTA** and that disbursement is Michael's action, not yours.

## Citations and confidentiality

Every statutory reference carries `[VERIFIED]` or `[VERIFY]`. Client facts stay in the file; any research uses genericized queries.

## Ethics screen

Run every letter past `firm/ethics.md` — fees (1.04), confidentiality (1.05), and, for anything a client reads, the line against giving legal advice (5.05). Flag, then draft.

## Output

- Write to `matters/<slug>/drafts/`, named `<type>-<yyyy-mm-dd>.docx` (or `.md`).
- Prefer **`.docx` via the `docx` skill** for letterhead; `.md` fallback.
- Drafts are Tier 1. **Sending any of these externally is Tier 2** — present ready-to-send and wait for approval.

## Close

Bottom line, `[VERIFY]` flags, and — if the letter is reusable — offer to generalize it into `templates/`.
