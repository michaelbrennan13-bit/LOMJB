# Intake

Where new-prospect work-ups land **before** a matter is opened. The `intake` skill writes summaries here.

## What lives here

One file per prospect, named `lastname-yyyy-mm-dd.md`, containing the intake package:

- Parties and facts summary
- Conflict-check list + the read-only Clio search result
- Limitations assessment (presumptive two-year PI limitations — **CPRC § 16.003 `[VERIFY]`** — with accrual date and tolling flags)
- Case-viability first pass (liability, coverage, damages → take / decline / need-more)
- A draft engagement letter **only if** Michael says take it

## Lifecycle

```
inbound inquiry  →  intake/<lastname>-<date>.md  →  [Michael's decision]
                                                       │
                                          take ────────┤────── decline
                                                       │
                                    matters/<slug>/  ◄──┘   (leave the intake file
                                    (matter-context             as the record of why)
                                     opens the matter)
```

An intake file becomes a matter only when Michael takes the case — then the `matter-context` skill opens `matters/<slug>/`. Declined intakes stay here as the record.

## Rules

- **Inbound only.** The firm responds to inquiries; it never drafts outbound solicitation to accident victims (barratry — **Tex. Penal Code § 38.12 `[VERIFY]`**).
- Prospect facts are confidential — they stay in this repo and Clio.
