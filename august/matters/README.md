# Matters

One folder per matter. Each is confidential client data — it stays in this repo, OneDrive/SharePoint, Clio, and firm email, and nowhere else.

## Naming convention

```
lastname-yyyy-shortdesc
```

- `lastname` — client's last name, lowercase.
- `yyyy` — year the matter opened.
- `shortdesc` — a couple of words on the matter, lowercase, hyphenated.

Examples:

- `garcia-2026-rearend`
- `nguyen-2025-premises`
- `okonkwo-2026-oilfield`
- `smith-2025-estate`

If a client has more than one matter, the `shortdesc` keeps them apart (`smith-2025-mvc`, `smith-2026-estate`).

## Folder structure

Every matter folder mirrors `_TEMPLATE/`:

```
matters/<slug>/
├── context.md     # Parties, facts, injuries, coverage, posture, key dates
├── contacts.md    # Client, adjusters, opposing counsel, providers, lienholders
└── drafts/        # Work product for this matter (demands, letters, memos)
```

## Opening a matter

Use the `matter-context` skill — it copies the template, pulls from Clio / SharePoint / email (read-only), and populates `context.md` and `contacts.md`. Other skills read `context.md` first, so keep it current (re-run `matter-context` to refresh).

## `_TEMPLATE/`

The skeleton copied for each new matter. Don't put real client data in `_TEMPLATE/` — it's the empty form.
