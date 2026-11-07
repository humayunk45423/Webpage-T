# Code Map & Coupling Hooks (`docs/CODE_MAP.md`)

## 1. Complete File Tree & Purpose

```text
Webpage-T/
├── index.html            # Main landing page: Hero, Diagnostic Services, Cost Estimator, Contact & Ethics
├── inventory.html        # Certified Smartphone Inventory Catalog (24+ devices, search, filter, sort)
├── 404.html              # Custom bilingual 404 error page with recovery links to Home and Inventory
├── style.css             # Complete stylesheet (tokens, dark/light themes, layout, components, breakpoints)
├── script.js             # Core client engine (theme, i18n dictionary, nav pill, drawer, estimator, inventory)
├── sw.js                 # PWA Service Worker (Stale-While-Revalidate caching for offline resilience)
├── manifest.json         # Web App Manifest (PWA metadata, theme colors, icons)
├── robots.txt            # Search crawler directives & sitemap pointer
├── sitemap.xml           # XML Sitemap with hreflang alternates (bn, en, x-default)
├── llms.txt              # Structured machine-readable business summary for AI search/assistants
├── Mobile Express.svg    # Primary vector brand mark & fallback image
└── assets/
    ├── logo.png          # Raster brand logo (OpenGraph, JSON-LD, PWA icon)
    └── logo.svg          # Vector brand logo copy
```

---

## 2. Pages, Sections & Component Usage

### 2.1 `index.html` (Home / Diagnostics & Service Center)
- **Background Layer:** `.parallax-environment` (`.ambient-glow`, `.ambient-glow-secondary`, `.ribbon-cluster`, `.card-band`, `.band-beam`) + `.grid-texture`
- **Header (`.glass-header` > `.nav-container`):**
  - `.brand` logo + title + motto (`[data-i18n="brand-motto"]`)
  - `.nav-links` with `.nav-pill-indicator` and 5 links: `#hero`, `#services`, `#estimator`, `#contact`, `inventory.html` (`.nav-count` `24+`)
  - `.nav-actions`: `#themeToggleBtn`, `#langToggleBtn`, `.btn-live-support` (WhatsApp), `#menu-toggle`
- **Mobile Navigation Drawer (`#drawer-overlay` + `aside#mobile-drawer`):**
  - `.drawer-header` (`.brand` + `#drawer-close`)
  - `.drawer-links` (5 navigation items)
  - `.drawer-segmented-wrapper` (`.theme-segmented-toggle`, `.lang-segmented-toggle`)
  - Full-width WhatsApp CTA (`.btn-primary.btn-full`)
- **Main (`main.app-content`):**
  1. `section#hero.hero-section.glass-panel`:
     - `.hero-badges-cluster` > `.hero-badge.apple-specialist-badge`
     - `h1.hero-title` (`[data-i18n="hero-title-1"]`, `.red-gradient-text[data-i18n="hero-title-2"]`)
     - `p.hero-desc[data-i18n="hero-desc"]` (contains `.location-highlight` Google Maps link)
     - `.hero-actions` (`a.btn-primary` -> `inventory.html`, `a.btn-secondary` -> `#services`)
     - `.hero-stats-row` (3 `.stat-box` items: `100+`, `99.4%`, `15 Mins`)
  2. `section#services.services-section`:
     - `h2.section-title`, `p.section-subtitle`
     - `.bento-grid` with 3 `.service-card.glass-panel` cards:
       - Card 1 (`.featured-apple-card`): Apple iCloud Lab (Create, Fix & Bypass) + `.service-meta-badge` + WhatsApp Inquire link
       - Card 2: FRP Account Removal + `.service-meta-badge` + WhatsApp Inquire link
       - Card 3: Dead Boot & Board Fix + `.service-meta-badge` + WhatsApp Inquire link
  3. `section#estimator.glass-panel.estimator-panel`:
     - `h2.section-title`, `p.section-subtitle`
     - `.calc-grid`:
       - `select#calc-brand.form-control` (`apple`, `android`)
       - `select#calc-issue.form-control` (`icloud`, `disabled`, `restore`, `frp`, `deadboot`, `network`, `hardware`)
       - `input#calc-model.form-control` (optional model text input)
       - `button#calc-btn.btn-primary`
     - `div#calc-result.calc-result`:
       - `#calc-result-title`, `#calc-result-desc`, `a#calc-wa-btn.btn-live-support`
  4. `section#contact.contact-section.glass-panel`:
     - `h2.section-title`, `p.section-subtitle`
     - `.contact-layout`:
       - `.card-pills` (3 `a.card-pill` items: Official WhatsApp Desk, Official Facebook Page, Shop Location on Google Maps)
       - `.qr-box` (`.qr-frame` with QR image + `.qr-whatsapp-icon` + `[data-i18n="qr-scan-label"]`)
     - `.ethics-box` (`p.ethics-text[data-i18n="ethics-text"]`, `span.ethics-ref[data-i18n="ethics-ref"]`)
- **Footer (`footer.site-footer`)** + **Floating WhatsApp (`a.floating-wa-btn`)**

### 2.2 `inventory.html` (Active Smartphone Inventory)
- Shares identical Header (`.glass-header`), Mobile Drawer (`#mobile-drawer`), Footer (`.site-footer`), and Floating WhatsApp (`.floating-wa-btn`) with `index.html`.
- **Main (`main.app-content` > `section.glass-panel.inv-main-panel`):**
  - `.hero-badges-cluster` (`.motto-badge`, `.apple-specialist-badge`)
  - `h1.section-title`, `p.section-subtitle`
  - `.inv-controls-wrapper`:
    - `.inv-search-bar`: `.search-input-wrap` > `input#inv-search` + `select#inv-sort.sort-dropdown` (`featured`, `price-low`, `price-high`, `name`)
    - `.brand-chips`: 9 `button.chip-btn` buttons (`data-filter="all"`, `"xiaomi"`, `"samsung"`, `"realme"`, `"vivo"`, `"oppo"`, `"infinix"`, `"oneplus"`, `"motorola"`)
    - `.inv-status-bar`: `span#inv-count.inv-count-badge` + `span.inv-guarantee-badge`
  - `div#inventory-grid.inv-grid`: Dynamically populated by `initInventoryCatalog()` in `script.js` with 24 `.inv-card` items (or an empty-state message when 0 items match).

### 2.3 `404.html` (Not Found Page)
- Minimal `.glass-header` with `.brand` link back to `index.html`.
- Centered `.glass-panel` with `404`, bilingual message, and 2 CTA buttons (`index.html`, `inventory.html`).

---

## 3. Global State, Event Listeners, Timers & Storage (`script.js`)

### 3.1 Global Variables & Constants
- `I18N_DICTIONARY` (`en` and `bn` translation maps, 66 keys each)
- `currentLanguage` (string, initialized from `localStorage.getItem('me_lang') || 'bn'`)
- `INVENTORY_DATA` (array of 24 smartphone objects: `id`, `brand`, `name`, `price`, `tag: {en, bn}`, `specs: string[]`, `img`)
- `window.reRenderInventory` (function exposed by `initInventoryCatalog()` so `initLanguageManager()` can re-render cards on language toggle)
- `window.refreshNavPill` (function exposed by `initNavPillSelector()` so `applyLanguage()` can reposition `.nav-pill-indicator` after text width changes)

### 3.2 Initialization & Event Listeners (`script.js`)
1. `document.addEventListener('DOMContentLoaded', ...)` calls 9 initializer functions:
   - `initThemeManager()`:
     - Reads `localStorage.getItem('me_theme') || 'light'`.
     - Attaches `click` listeners to `.theme-segmented-toggle, #themeToggleBtn, .theme-toggle-btn`.
     - Updates `document.documentElement.setAttribute('data-theme', theme)`, `data-state="left|right"`, `aria-label`, `title`, and `.theme-icon` classes.
   - `initLanguageManager()`:
     - Reads `localStorage.getItem('me_lang') || 'bn'`.
     - Attaches `click` listeners to `.lang-segmented-toggle, #langToggleBtn, .lang-toggle-btn`.
     - Toggles `document.body.classList.toggle('lang-bn', lang === 'bn')`.
     - Updates all `[data-i18n]` elements (`innerHTML` if value contains `<`, else `textContent`), updates `#inv-search` placeholder, calls `window.refreshNavPill()` and `window.reRenderInventory()`.
   - `initCrossingBandsParallax()`:
     - Attaches passive `scroll` listener using `requestAnimationFrame` to update `transform` on `.card-band, .band-beam` based on `data-speed`.
   - `initGlassNavbar()`:
     - Attaches passive `scroll` listener to toggle `.scrolled` on `.glass-header` when `window.scrollY > 30`.
   - `initNavPillSelector()`:
     - Manages `.nav-pill-indicator` position/width inside `.nav-links`.
     - Attaches `click` listeners on `.nav-links a` and `a[href^="#"]` for smooth scrolling with header offset (`80px` mobile / `105px` desktop) and `history.pushState`.
     - Attaches passive `scroll` spy on `index.html` for `#hero`, `#services`, `#estimator`, `#contact`.
     - Handles initial hash scroll on page load (`setTimeout` 50ms, 250ms, and `document.fonts.ready`).
     - Attaches `resize` listener to recalculate pill position.
   - `initMobileDrawer()`:
     - Attaches `click` listeners to `#menu-toggle` (opens drawer), `#drawer-close` (closes drawer), `#drawer-overlay` (closes drawer), and `.drawer-links a` (closes drawer + smooth scrolls).
     - Attaches `keydown` listener on `document` for `Escape` to close `#mobile-drawer`.
   - `initDiagnosticCalculator()`:
     - Attaches `click` listener to `#calc-btn`.
     - Reads `#calc-brand` and `#calc-issue` values (plus `#calc-model`).
     - Shows `alert()` if brand or issue is empty.
     - Looks up `database[category][issue][currentLanguage]` (or falls back to `'Custom Precision Diagnostics'`), updates `#calc-result-title`, `#calc-result-desc`, `#calc-wa-btn` `href`, adds `.visible` to `#calc-result`, and calls `resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' })`.
   - `initInventoryCatalog()`:
     - Attaches `input` listener to `#inv-search`, `change` listener to `#inv-sort`, and `click` listeners to `.chip-btn`.
     - Filters `INVENTORY_DATA` by `currentFilter` (note special groupings: `'xiaomi'` matches `'xiaomi'` and `'poco'`; `'infinix'` matches `'infinix'` and `'tecno'`) and `currentSearch` (matches `name`, `brand`, or any string in `specs`).
     - Sorts by `featured`, `price-low`, `price-high`, or `name`.
     - Updates `#inv-count` with localized count (`toBengaliDigits` in `bn`).
     - Renders `.inv-card` items into `#inventory-grid` (with `onerror` fallback on `<img>` to `'Mobile Express.svg'`).
   - `initServiceWorker()`:
     - Registers `./sw.js` on `window` `load` event on `https:`, `localhost`, or `127.0.0.1`.

---

## 4. DO-NOT-BREAK Coupling Hooks (Mandatory Preservation List)

Every identifier below is referenced by `script.js`, `sw.js`, CSS state rules, or external links and **MUST be preserved**:

### 4.1 DOM IDs
- `#hero`, `#services`, `#estimator`, `#contact` (Section IDs & scroll-spy targets)
- `#themeToggleBtn`, `#langToggleBtn` (Header segmented toggles)
- `#menu-toggle`, `#mobile-drawer`, `#drawer-overlay`, `#drawer-close` (Mobile navigation drawer)
- `#calc-brand`, `#calc-issue`, `#calc-model`, `#calc-btn`, `#calc-result`, `#calc-result-title`, `#calc-result-desc`, `#calc-wa-btn` (Diagnostic Estimator controls & output)
- `#inv-search`, `#inv-sort`, `#inv-count`, `#inventory-grid` (Inventory search, sort, counter, and grid container)

### 4.2 CSS Classes Referenced by JS
- `lang-bn` (toggled on `<body>` and `<html>`)
- `.glass-header`, `.scrolled` (navbar scroll state)
- `.nav-links`, `.nav-pill-indicator`, `.active` (navigation active tab & sliding indicator)
- `.drawer-links`, `.open`, `.active` (mobile drawer & overlay states)
- `.theme-segmented-toggle`, `.theme-toggle-btn`, `.theme-icon` (theme toggle hooks)
- `.lang-segmented-toggle`, `.lang-toggle-btn`, `.lang-label` (language toggle hooks)
- `.card-band`, `.band-beam`, `.band-left-outer`, `.band-left-main`, `.band-left-beam`, `.band-outer` (parallax hooks, safe if absent)
- `.visible` (toggled on `#calc-result`)
- `.chip-btn`, `.active` (inventory brand filter chips)
- `.inv-card`, `.inv-card-top`, `.inv-badge-top`, `.inv-brand`, `.inv-img`, `.inv-price`, `.inv-specs`, `.btn-primary`, `.btn-full` (rendered inside `#inventory-grid` by `script.js`)

### 4.3 Data Attributes & Storage Keys
- `data-theme="light|dark"` on `<html>`
- `data-state="left|right"` on `.segmented-toggle`
- `data-val="light|dark|bn|en"` on `.toggle-opt`
- `data-i18n="<key>"` on all translatable elements (all 66 keys in `I18N_DICTIONARY`)
- `data-filter="all|xiaomi|samsung|realme|vivo|oppo|infinix|oneplus|motorola"` on `.chip-btn`
- `data-speed` on `.card-band` / `.band-beam`
- `localStorage` keys: `me_theme`, `me_lang`
- Global window hooks: `window.reRenderInventory`, `window.refreshNavPill`
