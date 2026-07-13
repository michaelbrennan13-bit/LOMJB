# Law Office of Michael J. Brennan, PLLC — Website

Marketing site for a Texas general-practice law firm (personal injury flagship),
serving Fort Bend County & Greater Houston.

- **Stack:** [Astro](https://astro.build) (static/SSG) + [Tailwind CSS v4](https://tailwindcss.com)
- **Fonts:** Cinzel + Montserrat, self-hosted via `@fontsource` (no external font requests)
- **Hosting:** Cloudflare Pages, domain `mjbrennan.com`
- **JS on the page:** only the mobile-nav toggle and the contact-form submit

---

## 1. Local development

This project needs **Node.js 18+** (Node 24 LTS recommended) and npm.

```bash
# from the project root (this folder)
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
public/
  assets/                    # brand SVGs, favicon, apple-touch, OG image, headshot stub
  robots.txt
src/
  consts.ts                  # ← site-wide values + PLACEHOLDERS (phone, email, key, hours)
  data/practices.ts          # practice-area content (editable)
  styles/global.css          # brand tokens (navy/burgundy/gold/warmgrey/charcoal) + base
  layouts/Layout.astro       # <head>, SEO/OG, JSON-LD, skip link, Header + Footer
  components/
    Header.astro             # sticky header, inline logo, mobile hamburger
    Footer.astro             # navy band + compliance block
    PracticeIcon.astro       # gold-line practice icons
  pages/
    index.astro              # Home
    about.astro              # About
    practice-areas.astro     # Practice Areas
    contact.astro            # Contact (Web3Forms form)
astro.config.mjs             # site URL, Tailwind (via @tailwindcss/vite), sitemap
```

### A note on the logo

The three **text-bearing lockups** (horizontal header logo, footer banner) are
**inlined as SVG** in `Header.astro` / `Footer.astro` so the wordmark renders in
Cinzel/Montserrat. (An SVG loaded via `<img>` cannot use the page's web fonts and
would fall back to a generic serif.) The original files still live in
`public/assets/` and are used for the favicon, Apple touch icon, and OG image.
The seal-only marks are pure geometry and are safe to reference as `<img>`.

---

## 3. Placeholder checklist (fill before go-live)

Most placeholders live in **`src/consts.ts`** unless noted.

- [ ] **Phone** — `SITE.phone` and `SITE.phoneHref` (digits only, e.g. `+12815551234`)
- [ ] **Contact email** — `SITE.email`
- [ ] **Office hours** — `SITE.hours`
- [ ] **Web3Forms access key** — `SITE.web3formsKey` — get a free key at
      <https://web3forms.com> (used by the contact form)
- [ ] **Attorney headshot** — replace `public/assets/headshot-placeholder.svg`
      with a real photo. If you add `headshot-placeholder.jpg`, update the
      `<img src>` in `src/pages/about.astro`.
- [ ] **Attorney bio** — `src/pages/about.astro`: fill the bracketed
      `[PLACEHOLDER]` / `[degree]` / `[law school]` / `[year]` / `[background]`
      blanks (highlighted on the page).
- [ ] **Education / admissions** — About page "Credentials" list.
- [ ] **"[confirm]" experience claim** — Home positioning band (only keep the
      "both sides of the docket" line if accurate).
- [ ] **Contingency cost disclosure** — confirm the wording in
      `COMPLIANCE.contingencyCosts` (`src/consts.ts`) against the actual fee
      agreement; edit the bracketed sentence about who owes costs.

Already final (no action needed): logo SVGs, `favicon.ico`,
`apple-touch-icon.png`, `og-image.png` — all in `public/assets/`.

---

## 4. Compliance (Texas Disciplinary Rules, Part VII)

These are implemented in the footer (every page) and on relevant pages. **Do not
remove them**, and re-check them if you edit copy:

- Responsible attorney + principal office city (Houston) — footer, every page.
- State Bar No. 24125746 — footer.
- **No** "specialist / expert / specializing / certified" language anywhere
  (the attorney is not Board Certified). Use "focuses on," "handles,"
  "practices in."
- Contingent-fee **cost disclosure** wherever contingency is mentioned
  (Home, Practice Areas).
- "Past results do not guarantee, warrant, or predict future outcomes."
- "Not legal advice / no attorney-client relationship" — footer + contact page.

---

## 5. Deploy to Cloudflare Pages

The domain is already in this Cloudflare account, so DNS records for the site are
created automatically when you attach the custom domain.

### 5.1 Push to GitHub

```bash
git init
git add -A
git commit -m "Initial site for Law Office of Michael J. Brennan, PLLC"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
```

### 5.2 Create the Pages project

1. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git**.
2. Select the repo.
3. Build settings:
   - **Framework preset:** Astro
   - **Build command:** `npm run build`
   - **Build output directory:** `dist`
4. **Save and Deploy.**

### 5.3 Custom domain

- Pages project → **Custom domains** → add `mjbrennan.com` **and**
  `www.mjbrennan.com`.
- Because DNS is already in this Cloudflare account, the records + SSL provision
  automatically.

### 5.4 www → apex redirect

Add a **Redirect Rule** (Rules → Redirect Rules): if hostname equals
`www.mjbrennan.com`, redirect (301) to `https://mjbrennan.com/$1` preserving path.
(Or configure the reverse if you prefer `www` as canonical — then also update
`site` in `astro.config.mjs`.)

### 5.5 ⚠️ Do NOT touch Microsoft 365 mail DNS

Leave all existing **MX**, **SPF** (TXT), **DKIM**, and **autodiscover** records
untouched. Only the web records for the apex + `www` should be added (Pages does
this automatically). After go-live, **send a test email** to confirm mail still
flows.

---

## 6. SEO / technical notes

- Per-page `<title>` + meta description; canonical URLs.
- JSON-LD `LegalService` / `Attorney` schema in `Layout.astro`.
- Open Graph + Twitter card using `/assets/og-image.png`.
- `sitemap-index.xml` generated by `@astrojs/sitemap`; `robots.txt` in `public/`.
- Accessibility: semantic landmarks, skip link, visible focus states, alt text,
  AA-contrast palette (gold used only for decorative/large elements).
- Update the production URL in `astro.config.mjs` (`site`) if the canonical
  domain changes.
