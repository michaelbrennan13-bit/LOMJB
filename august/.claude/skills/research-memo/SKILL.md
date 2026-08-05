---
name: research-memo
description: Research a Texas (or federal) legal question and write a memo with a Fastcase/vLex search plan. Use when Michael asks a legal question, says "research whether/how <question>," "write me a memo on <issue>," "what's the law on," or "look into <legal topic>." Produces a memo to research/memos/ with every authority marked VERIFIED or VERIFY.
---

# Research Memo

Answer a legal question in a structured memo. You cannot run Fastcase/vLex (browser-only, no API), so you deliver your analysis **plus** an exact search plan Michael runs to verify — and you fetch free authorities directly to upgrade cites to VERIFIED.

## Input

A legal question. If it's tied to a matter, note the matter but **genericize** the question for any web research (no client names or identifying facts).

## Workflow

1. **Frame the question.** Restate it as a clean legal question. If it has sub-questions, list them.

2. **Fetch what you can, for free.** Before writing from memory, pull authoritative free sources and read them:
   - **Texas statutes:** `statutes.capitol.texas.gov` — fetch the actual code section.
   - **Opinions:** CourtListener — read the opinion, don't infer it.
   - Any cite you actually read this session becomes **`[VERIFIED — source]`**.

3. **Write the memo** (structure below). Everything you didn't fetch and read is **`[VERIFY — what to check and where]`**. Never smooth over an uncertain cite.

4. **Build the search plan.** The exact Fastcase/vLex queries Michael should run, ranked by expected yield, each with what it's meant to confirm.

## Memo structure

```
# Research Memo — <topic>
Date: <yyyy-mm-dd>   |   Prepared by: August   |   Matter: <slug or "general">

## Question Presented
<the clean legal question, and sub-questions if any>

## Short Answer
<bottom line first — the answer in 2–4 sentences, with confidence level and the
biggest open question>

## Analysis
<the reasoning. Every case, statute, rule, and holding carries an inline
[VERIFIED — source] or [VERIFY — what/where] marker. Distinguish settled law
from your read of unsettled law. Note splits, exceptions, and how Texas courts
have actually applied the rule where you know it.>

## Fastcase / vLex Search Plan
Ranked by expected yield. Run in order; stop when confirmed.

1. Query: `<exact search string>`
   - Confirms: <what this search is meant to establish>
   - Expected yield: high/medium/low
2. Query: `<exact search string>`
   - Confirms: ...
...

## Verification Checklist
- [ ] <authority> — <what to confirm> — <where>
- [ ] ...

## Open Questions / What I Couldn't Verify
<honest list of what remains uncertain and why>
```

## Rules

- **Citation discipline is absolute.** No invented or approximated cites, case names, statute/rule numbers, or holdings. Ever. See CLAUDE.md.
- **Confidentiality:** genericized queries only. The legal question goes to the web; the client's story does not.
- The memo is Tier 1 (writing your own research). It's a work product for Michael, not advice to a client.

## Output

- Write to `research/memos/<yyyy-mm-dd>-<topic-slug>.md`.
- `.md` is fine for memos; use `.docx` only if Michael wants it formatted for a file.

## Close

Bottom line first: the short answer, the count of VERIFIED vs. VERIFY cites, and the top 1–2 searches that would resolve the biggest open question.
