# LOMJB — Law Office of Michael J. Brennan, PLLC (Website)

Design & build spec for the marketing site of a Texas **full-service** law firm
(personal injury flagship), serving Fort Bend County & Greater Houston.

Throughout this document and the repo, **LOMJB** is the project designation. All
website files live under the `LOMJB/` folder (this repo is `LOMJB/Website/`), and
any path below is relative to `LOMJB/Website/` unless stated otherwise.

- **Stack:** [Astro](https://astro.build) (static/SSG) + [Tailwind CSS v4](https://tailwindcss.com)
- **Fonts:** Cinzel + Montserrat, self-hosted via `@fontsource` (no external font requests)
- **Hosting:** Cloudflare Pages, domain `mjbrennan.com`
- **JS on the page:** only the mobile-nav toggle and the contact-form submit

---

## 0. Provided assets (in `LOMJB/`)

These real assets are now available and should replace the earlier placeholders:

- **`LOMJB/Website/Firm Bio.docx`** — the authoritative attorney bio. Use it to
  fill the About page (see §7). Do not paraphrase in ways that add
  specialist/expert claims (see §5 compliance).
- **`LOMJB/Website/Headshot.jpeg`** — the attorney headshot. Optimize and place it
  at `public/assets/headshot.jpg` (or `.webp`), then update the `<img src>` in
  `src/pages/about.astro` and remove `headshot-placeholder.svg`.

When editing, keep source assets in `LOMJB/` and the web-ready, optimized copies
in `public/assets/`.

---

## 1. Local development

This project needs **Node.js 18+** (Node 24 LTS recommended) and npm.

```bash
# from the project root (LOMJB/Website)
npm install
npm run dev        # http://localhost:4321
```

Other commands:

```bash
npm run build      # production build → ./dist
npm run preview    # serve the built ./dist locally to verify
```

> **Note on Node:** if `node` / `npm` are not found, install Node from
> <https://nodejs.org> (LTS) or via a version manager (`nvm`, `fnm`, Homebrew
> `brew install node`). Cloudflare Pages installs Node on its build servers, so
> you do **not** need Node locally just to deploy — only for local preview.

---

## 2. Project structure

```
LOMJB/Website/
  Firm Bio.docx              # source: attorney bio (see §0, §7)
  Headshot.jpeg              # source: attorney headshot (see §0)
  public/
    assets/                  # brand SVGs, favicon, apple-touch, OG image, headshot
    robots.txt
  src/
    consts.ts                # ← site-wide values + PLACEHOLDERS (phone, email, key, hours)
    data/practices.ts        # practice-area content (editable) — see §6
    styles/global.css        # brand tokens (navy/burgundy/gold/warmgrey/charcoal) + base
    layouts/Layout.astro     # <head>, SEO/OG, JSON-LD, skip link, Header + Footer
    components/
      Header.astro           # sticky header, inline logo, mobile hamburger
      Footer.astro           # navy band + compliance block
      PracticeIcon.astro     # gold-line practice icons
    pages/
      index.astro            # Home
      about.astro            # About
      practice-areas.astro   # Practice Areas
      contact.astro          # Contact (Web3Forms form)
  astro.config.mjs           # site URL, Tailwind (via @tailwindcss/vite), sitemap
```

### A note on the logo

The three **text-bearing lockups** (horizontal header logo, footer banner) are
**inlined as SVG** in `Header.astro` / `Footer.astro` so the wordmark renders in
Cinzel/Montserrat. (An SVG loaded via `<img>` cannot use the page's web fonts and
would fall back to a generic serif.) The original files still live in
`public/assets/` and are used for the favicon, Apple touch icon, and OG image.
The seal-only marks are pure geometry and are safe to reference as `<img>`.

---

## 3. Design direction — make it distinctive, not "vibe-coded"

**Goal:** the site should look like it was designed for *this* firm by a person
with taste — not like a generic AI/template landing page. Reviewers should not be
able to guess it was scaffolded from a starter. Treat the following as binding
design constraints, not suggestions.

**Avoid these tells of generic "vibe coding":**

- The default template skeleton: full-width centered hero → one headline → one
  sub-line → two pill buttons → a symmetric row of three identical feature cards.
- Purple/indigo gradients, glowing "gradient blobs," glassmorphism, and neon
  accents. They do not belong on a law firm site and read as AI-default.
- Emoji as icons, generic stock "handshake/gavel/scales" clip art, and
  lorem-ipsum rhythm where every section is the same height and centered.
- Uniform, evenly-spaced cards with identical drop shadows and rounded-2xl
  corners everywhere; oversized hero text with no typographic hierarchy.
- Tailwind defaults left untouched (indigo-600 buttons, `container mx-auto`
  everything, `text-gray-500` body). Everything should come from our brand
  tokens.

**Do this instead — a considered, editorial identity:**

- **Own the brand palette.** Build strictly from the tokens in `global.css`
  (deep navy, burgundy, gold, warm grey, charcoal). Gold is an *accent* for
  rules, seal, and large decorative elements only — never for body text or small
  UI (contrast/compliance, §5). No colors outside the token set.
- **Editorial layout, not a landing-page stack.** Use asymmetry and a real grid:
  left-aligned hero with the seal/wordmark and generous negative space; sections
  that vary in rhythm and alignment rather than a monotonous centered column.
  Establish a 12-column grid and let content break it intentionally.
- **Typography with hierarchy.** Cinzel for display/wordmark, Montserrat for
  body and UI. Set a real type scale (distinct display / H1 / H2 / body / caption
  sizes and weights), comfortable measure (~60–75 characters), and consistent
  vertical rhythm. Let headings carry the design — avoid decorative gimmicks.
- **Signature detail from the brand mark.** Derive a recurring motif from the
  firm seal (e.g., a thin gold hairline rule, a small seal glyph as a section
  marker, or a subtle letterpress-style divider). Reuse it so the site feels
  authored and cohesive.
- **Custom, consistent iconography.** Keep the thin gold-line practice icons in
  `PracticeIcon.astro`; extend the same stroke weight and style to any new
  practice area (§6). No mixing icon libraries or emoji.
- **Real photography and texture.** Use the provided headshot (§0) and, where
  imagery is needed, favor restrained real photography (Houston/Fort Bend
  context) or subtle paper/texture over flat gradients. Duotone toward navy for
  cohesion if using photos.
- **Restraint and craft.** Tight, purposeful spacing; one or two accent moments
  per page, not on every element; hover/focus states that are subtle and
  consistent; motion (if any) limited to small, tasteful transitions — never
  parallax gimmickry.

**Litmus test before shipping any page:** Would this look at home in a printed
firm brochure or on a bespoke boutique-firm site? If it instead looks like a SaaS
starter template, revise it.

---

## 4. Placeholder checklist (fill before go-live)

Most placeholders live in **`src/consts.ts`** unless noted.

- [ ] **Phone** — `SITE.phone` and `SITE.phoneHref` (digits only, e.g. `+12815551234`)
- [ ] **Contact email** — `SITE.email`
- [ ] **Office hours** — `SITE.hours`
- [ ] **Web3Forms access key** — `SITE.web3formsKey` — get a free key at
      <https://web3forms.com> (used by the contact form)
- [x] **Attorney headshot** — provided: `LOMJB/Website/Headshot.jpeg`. Optimize
      to `public/assets/headshot.jpg`/`.webp` and update the `<img src>` in
      `src/pages/about.astro`; remove the placeholder SVG.
- [x] **Attorney bio** — provided: `LOMJB/Website/Firm Bio.docx`. Populate the
      About page from it (see §7); remove bracketed `[PLACEHOLDER]` blanks.
- [x] **Education / admissions** — from the bio: Baylor University (BBA), Texas
      A&M University School of Law (JD); admitted in all Texas state courts and
      the Southern, Eastern, and Western Districts of Texas.
- [ ] **"[confirm]" experience claim** — Home positioning band. The bio supports
      a defense-side background ("both sides of the docket") — keep only if you're
      comfortable stating it publicly.
- [ ] **Contingency cost disclosure** — confirm the wording in
      `COMPLIANCE.contingencyCosts` (`src/consts.ts`) against the actual fee
      agreement; edit the bracketed sentence about who owes costs.

Already final (no action needed): logo SVGs, `favicon.ico`,
`apple-touch-icon.png`, `og-image.png` — all in `public/assets/`.

---

## 5. Compliance (Texas Disciplinary Rules, Part VII)

These are implemented in the footer (every page) and on relevant pages. **Do not
remove them**, and re-check them if you edit copy:

- Responsible attorney + principal office city (Houston) — footer, every page.
- State Bar No. 24125746 — footer.
- **No** "specialist / expert / specializing / certified" language anywhere
  (the attorney is not Board Certified). Use "focuses on," "handles,"
  "practices in." This applies to every new practice area added in §6.
- Contingent-fee **cost disclosure** wherever contingency is mentioned. Only the
  injury areas (Personal Injury, Wrongful Death, and Insurance Disputes handled
  on contingency) carry contingency messaging; flat/hourly areas must not imply
  "no fee unless we win."
- "Past results do not guarantee, warrant, or predict future outcomes."
- "Not legal advice / no attorney-client relationship" — footer + contact page.

---

## 6. Practice areas — full-service, personal injury first

The firm is presented as **full-service, with Personal Injury first and
emphasized** (flagship). All practice content lives in `src/data/practices.ts`;
the Home grid and Practice Areas page both read from it. Keep Personal Injury as
the lead card, then the remaining areas in the order below.

Fee model per area (drives the `contingency` flag and copy):

| # | Practice area | Fee model | Contingency copy? |
|---|---------------|-----------|-------------------|
| 1 | **Personal Injury** (flagship) | Contingency | Yes |
| 2 | Wrongful Death | Contingency | Yes |
| 3 | Insurance Disputes (denied / bad-faith claims) | Contingency or hourly | Yes (when contingent) |
| 4 | Business & Commercial (formation & disputes) | Flat / hourly | No |
| 5 | Contract Drafting & Review | Flat / hourly | No |
| 6 | Family Law (divorce, custody, support) | Flat / hourly | No |
| 7 | Consumer & Debt Defense | Flat / hourly | No |
| 8 | Estate Planning & Wills | Flat / hourly | No |
| 9 | Probate & Guardianship | Flat / hourly | No |
| 10 | Civil Litigation | Flat / hourly | No |
| 11 | Landlord–Tenant / Real Estate | Flat / hourly | No |

**Newly added areas (this revision):** Insurance Disputes, Business & Commercial,
Contract Drafting & Review, Family Law, Consumer & Debt Defense, and Probate &
Guardianship. When implementing:

- Extend the `IconName` union in `practices.ts` and add a matching thin gold-line
  icon in `PracticeIcon.astro` for each new area (same stroke/style — see §3).
- Write each `detail` as a candid, non-promissory paragraph in the firm's voice.
  For new areas, describe *what the firm handles* and the fee model up front; do
  not promise outcomes and do not use specialist language (§5).
- Group tightly related items in the UI if the grid gets long (e.g., present
  "Business & Commercial" and "Contract Drafting & Review" as siblings, and
  "Estate Planning & Wills" with "Probate & Guardianship"), but keep each as its
  own entry in the data file so it's individually addressable for SEO.
- Update JSON-LD (`Layout.astro`) `areaServed` / service list and the Practice
  Areas page navigation to include all areas.

Suggested one-line blurbs (edit to taste; keep non-promissory):

- **Insurance Disputes** — "Fighting denied, delayed, and underpaid insurance
  claims — including first-party property and bad-faith disputes."
- **Business & Commercial** — "Entity formation and commercial disputes for small
  businesses and their owners."
- **Contract Drafting & Review** — "Clear contracts drafted and reviewed before
  you sign — for individuals and small businesses."
- **Family Law** — "Divorce, custody, support, and modifications, handled with
  discretion."
- **Consumer & Debt Defense** — "Defense against debt-collection suits and
  consumer-protection matters."
- **Probate & Guardianship** — "Guiding families through probate, estate
  administration, and guardianships."

---

## 7. About page — from the firm bio

Populate `src/pages/about.astro` from `LOMJB/Website/Firm Bio.docx`. Key facts:

- Houston-area native; former defense-side litigator (corporate defendants in
  complex personal injury and wrongful death — Gulf Coast industrial accidents,
  interstate trucking/commercial fleet, oilfield/industrial workplace, premises
  liability) who now represents plaintiffs. This is the "both sides of the
  docket" positioning referenced in §4.
- Solo practitioner offering direct, personal attention at every stage.
- **Education:** Baylor University (BBA); Texas A&M University School of Law (JD).
- **Court admissions:** all Texas state courts; U.S. District Courts for the
  Southern, Eastern, and Western Districts of Texas.
- **Memberships:** Houston Young Lawyers Association; Houston Trial Lawyers
  Association; Texas Trial Lawyers Association (Lead Academy 2026).
- **Personal:** walking his dogs along the Hershey Trails, golfing, reading.
- **Values:** integrity, personal service, relentless advocacy.

Keep the bio's own wording where possible; do not introduce "expert/specialist"
phrasing (§5). Place the optimized headshot alongside the bio text.

---

## 8. Deploy to Cloudflare Pages

The domain is already in this Cloudflare account, so DNS records for the site are
created automatically when you attach the custom domain.

### 8.1 Push to GitHub

```bash
git init
git add -A
git commit -m "LOMJB site — Law Office of Michael J. Brennan, PLLC"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
```

### 8.2 Create the Pages project

1. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git**.
2. Select the repo.
3. Build settings:
   - **Framework preset:** Astro
   - **Build command:** `npm run build`
   - **Build output directory:** `dist`
4. **Save and Deploy.**

### 8.3 Custom domain

- Pages project → **Custom domains** → add `mjbrennan.com` **and**
  `www.mjbrennan.com`.
- Because DNS is already in this Cloudflare account, the records + SSL provision
  automatically.

### 8.4 www → apex redirect

Add a **Redirect Rule** (Rules → Redirect Rules): if hostname equals
`www.mjbrennan.com`, redirect (301) to `https://mjbrennan.com/$1` preserving path.
(Or configure the reverse if you prefer `www` as canonical — then also update
`site` in `astro.config.mjs`.)

### 8.5 ⚠️ Do NOT touch Microsoft 365 mail DNS

Leave all existing **MX**, **SPF** (TXT), **DKIM**, and **autodiscover** records
untouched. Only the web records for the apex + `www` should be added (Pages does
this automatically). After go-live, **send a test email** to confirm mail still
flows.

---

## 9. SEO / technical notes

- Per-page `<title>` + meta description; canonical URLs. Give each practice area
  (§6) its own descriptive title/description for search.
- JSON-LD `LegalService` / `Attorney` schema in `Layout.astro`; list all practice
  areas in the service schema.
- Open Graph + Twitter card using `/assets/og-image.png`.
- `sitemap-index.xml` generated by `@astrojs/sitemap`; `robots.txt` in `public/`.
- Accessibility: semantic landmarks, skip link, visible focus states, alt text,
  AA-contrast palette (gold used only for decorative/large elements).
- Update the production URL in `astro.config.mjs` (`site`) if the canonical
  domain changes.
