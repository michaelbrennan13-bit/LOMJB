---
name: retro
description: Capture a correction from Michael so the same fix never has to be made twice — log it to ops/decisions.md and update the relevant skill or voice file. Use when Michael says "retro," corrects your work, tells you to stop or start doing something, gives a formatting or workflow preference, or sends a voice note with feedback.
---

# Retro

The learning loop. This is how you grow with the firm: every correction becomes a durable change to your instructions, not a thing Michael has to repeat. Invoked as "retro," or run it yourself right after any correction.

## Workflow

1. **Identify the correction.** What did Michael change? If he said it explicitly ("stop using the word 'moreover'"), take it verbatim. If it's implicit (he edited your draft, rejected an approach, restated a preference), infer the rule and **state your inference back in one line** so he can confirm or fix it.

2. **Log it to `ops/decisions.md`.** Append an entry — never overwrite. Format:

```
## <yyyy-mm-dd> — <short title>
**Correction:** <what Michael changed or asked for>
**Rule going forward:** <the durable rule, stated so a future session can apply it>
**Applied to:** <file(s) you edited — or "log only" if no file change fits>
```

3. **Make it stick — edit the right file.** A log entry alone won't change behavior; update the instruction that will:
   - Voice / word choice / tone → `firm/voice.md`.
   - How a specific deliverable is built → that skill's `SKILL.md`.
   - A cross-cutting rule (tier, citation, confidentiality, routing) → `CLAUDE.md`.
   - A firm fact (address, stack, referral) → `firm/profile.md`.
   - An ethics screening change → `firm/ethics.md`.

4. **Show the diff.** Display exactly what changed in the file(s) so Michael can confirm the correction landed the way he meant. Keep edits surgical — change the rule, don't rewrite the file.

## Rules

- **Append to `decisions.md`, never overwrite** — it's the history of how the firm's preferences evolved.
- Editing your own memory and instruction files is **Tier 1**. Do it, then show the diff.
- If a correction conflicts with an existing rule, note the conflict in the log entry and update the older rule so they don't fight.
- One correction, one durable change. Don't over-engineer; make the smallest edit that captures the rule.

## Output

Bottom line: the rule you captured (one line), the file(s) you changed, and the diff. If you inferred the rule rather than being told, ask Michael to confirm in the same line.
