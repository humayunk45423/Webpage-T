# Baseline Issues Log (`docs/BASELINE_ISSUES.md`)

Documented at baseline (`baseline-before-redesign` tag, commit `ef82cac`) before any code modifications.

## 1. Network / External Image Failures at Baseline
When loading `inventory.html` in a real Chromium browser via Playwright, 4 of the 24 external GSMArena handset image URLs fail with `net::ERR_BLOCKED_BY_ORB` (Opaque Response Blocking / missing or moved upstream image on `fdn2.gsmarena.com`):
1. `https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-12.jpg` (`id: 2`, Xiaomi Redmi Note 12)
2. `https://fdn2.gsmarena.com/vv/bigpic/realme-10-4g.jpg` (`id: 8`, Realme 10)
3. `https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a24-4g.jpg` (`id: 10`, Samsung Galaxy A24)
4. `https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-m14-5g.jpg` (`id: 11`, Samsung Galaxy M14 5G)

- **Baseline Behavior:** The `<img>` `onerror="this.onerror=null; this.src='Mobile Express.svg';"` handler triggers and replaces the broken image with `Mobile Express.svg`, while logging `net::ERR_BLOCKED_BY_ORB` on those 4 network requests.

## 2. CSS `content-visibility: auto` Rendering Defect on `inventory.html`
- In `style.css` lines 1687–1688, `.inv-card` has `content-visibility: auto; contain-intrinsic-size: 1px 360px;`.
- At baseline, below-the-fold cards (cards 13–24 on desktop) render as empty blank card boxes in full-page screenshots and cause layout jump when scrolling rapidly.

## 3. Incomplete Bilingual (`bn`/`en`) Localization at Baseline
- Default language is Bengali (`bn`), but the following interactive controls lack `data-i18n` attributes and remain hardcoded in English even when `bn` is active:
  - `index.html`: `#calc-brand` options (`Select Platform...`, `Apple (iPhone / iPad)`, `Android (Samsung / Xiaomi / etc.)`)
  - `index.html`: `#calc-issue` options (`Select Issue...`, `iCloud Activation Lock`, `iPhone Disabled / Unavailable`, `Unable to Activate / Baseband`, `Android Google FRP Lock`, `Dead Boot / Qualcomm 9008`, `SIM Carrier / Region Locked`, `Motherboard Power Short`)
  - `index.html`: `#calc-model` placeholder (`e.g. iPhone 13, Note 12`)
  - `index.html`: `#calc-wa-btn` label (`Confirm on WhatsApp`)
  - `inventory.html`: `#inv-sort` options (`Sort: Featured`, `Price: Low to High`, `Price: High to Low`, `Name: A to Z`)
  - `404.html`: Does not include `script.js`, so theme (`me_theme`) and language (`me_lang`) preferences are not applied, and the paragraph body is hardcoded in English while the heading and buttons are hardcoded in Bengali.

## 4. Accessibility & Impeccable Detector Violations at Baseline
Running `.agents\skills\impeccable\scripts\impeccable.cmd detect --json index.html inventory.html 404.html` at baseline returned **47 findings** across `index.html`, `inventory.html`, and `404.html`:
- **Focus Ring Suppression (`style.css:134-140`):** `button:focus, button:focus-visible, a:focus, a:focus-visible { outline: none !important; box-shadow: none; }` removes keyboard focus indicators globally.
- **WCAG AA Contrast Failures:**
  - `.btn-live-support` & `#calc-wa-btn`: `#ffffff` text on `#25d366` background = **2.0:1** (requires ≥ 4.5:1).
  - `.inv-guarantee-badge`: `#25d366` text on light panel `#fdfefe` = **2.0:1** (requires ≥ 4.5:1).
  - `.featured-tag` / `.inv-badge-top`: `#ef233c` / `#d90429` text on `#fbebee` = **3.4:1 – 3.7:1** (requires ≥ 4.5:1).
  - `--text-dim` (`#64748b`) on `--bg-dark` (`#f3f5f9`) in light mode = **4.4:1** (requires ≥ 4.5:1).
- **Undersized UI Text (< 11px floor):**
  - `.nav-count` (`0.64rem` = `10.24px`)
  - `.pill-content span` (`0.65rem`–`0.72rem` = `10.4px`)
  - Mobile `.inv-badge-top` (`0.54rem` = `8.64px`), `.inv-brand` (`0.56rem` = `8.96px`), `.inv-specs` (`0.62rem` = `9.92px`), `.stat-box span` (`0.58rem` = `9.28px`).
- **Undersized Touch Targets on Mobile (< 44×44px):**
  - `#menu-toggle` on mobile (`<= 960px`) is `36px × 36px`.
  - `.chip-btn` on mobile (`<= 640px`) is `29px` tall (`padding: 6px 14px`).
  - `.segmented-toggle` is `36px` tall (`width: 68px; height: 36px`).
- **AI-Slop Visual Patterns Flagged by Detector:**
  - `pulsing-dot` (severity: `error`): `.pulse-indicator` infinite `pulseRing` animation in header.
  - `gradient-text` (severity: `warning`): `.red-gradient-text` on hero headline.
  - `side-tab` (severity: `warning`): `border-left: 4px solid var(--red-main)` on `.calc-result`.
  - `icon-tile-stack` (severity: `warning`): `.s-icon-box` square icon container stacked above `h3` in `.service-card`.
  - `dark-glow` (severity: `warning`): Colored red `box-shadow` glow (`--shadow-glow`).
  - `codex-grid-background` (severity: `advisory`): `.grid-texture` two-axis hairline grid overlay.
  - `nested-cards` (severity: `warning`): Cards nested inside `.glass-panel` containers (`section.glass-panel.inv-main-panel` > `.inv-card`, `section.contact-section.glass-panel` > `.card-pill`).
  - `bounce-easing` (severity: `advisory`): `cubic-bezier(0.34, 1.56, 0.64, 1)` overshoot easing.
  - `overused-font` (severity: `warning`): `Plus Jakarta Sans` as primary display/body font.
