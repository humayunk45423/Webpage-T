# Redesign Plan (`docs/REDESIGN_PLAN.md`)

## 1. Page-by-Page Layout Plan & Component Architecture

### 1.1 Global Shell (`index.html`, `inventory.html`, `404.html`)
- **Skip-to-Content Link (`.skip-link`):** Keyboard-accessible skip link to `#main-content`.
- **Sticky Frosted Top Header (`header.glass-header` > `nav.nav-container`):**
  - Left: `a.brand` (`Mobile Express.svg` + `Mobile Express` + localized motto `[data-i18n="brand-motto"]`).
  - Center (Desktop): `.nav-links` with `.nav-pill-indicator` and 5 primary navigation items (`Home`, `Diagnostics`, `Estimator`, `Contact`, `Inventory 24+`).
  - Right (`.nav-actions`):
    - Theme Segmented Toggle (`#themeToggleBtn.segmented-toggle.theme-segmented-toggle`)
    - Language Segmented Toggle (`#langToggleBtn.segmented-toggle.lang-segmented-toggle` — kept visible on mobile too or paired with a quick mobile language switcher so non-technical users can switch `বাং / EN` in 1 tap without opening the drawer!)
    - WhatsApp Live Support CTA (`a.btn-live-support`) with static online badge (no infinite pulse)
    - Mobile Hamburger Button (`button#menu-toggle.menu-toggle`, `44×44px` minimum hit target)
- **Mobile Navigation Drawer (`#drawer-overlay` + `aside#mobile-drawer`):**
  - Clean slide-over sheet (`overscroll-behavior: contain`) with `.drawer-header`, `#drawer-close` (`44×44px`), `.drawer-links`, `.drawer-segmented-wrapper` (Theme & Language toggles), and full-width WhatsApp CTA.
- **Footer (`footer.site-footer`) & Floating WhatsApp Button (`a.floating-wa-btn`):**
  - Positioned safely so it never overlaps interactive cards or badges at any viewport width (`360px`–`1920px`).

### 1.2 `index.html` — Home / Diagnostics & Service Center
1. **Hero Section (`section#hero.hero-section`):**
   - Clean, high-contrast Apple-inspired showroom surface (`#ffffff` light / `#141417` dark, `18px` radius, `1px solid` hairline border).
   - Specialist badge (`.hero-badge.apple-specialist-badge`), solid high-impact `h1.hero-title` (no gradient text), plain-language `p.hero-desc` with Google Maps `.location-highlight` pill link.
   - Two clear action buttons in `.hero-actions`:
     - Primary Action (`a.btn-primary` -> `inventory.html`): *"Buy / Exchange Phones (24+)"* / *"স্মার্টফোন দেখুন ও এক্সচেঞ্জ (২৪+)"*
     - Secondary Action (`a.btn-secondary` -> `#estimator` / `#services`): *"Apple & iCloud Lab"* / *"অ্যাপল ও আইক্লাউড ল্যাব"*
   - Trust Metrics Bar (`.hero-stats-row`): 3 balanced stat cells (`100+ Devices Restored`, `99.4% Bypass Success Rate`, `15 Mins Express Turnaround`) with `tabular-nums` and readable ≥ `12px` labels.
2. **Diagnostic Services Section (`section#services.services-section`):**
   - Section header (`h2.section-title` + `p.section-subtitle`).
   - 3-column `.bento-grid` of `.service-card` utility cards (no nested `.glass-panel` inside `.glass-panel`, no stacked icon-tile above heading — instead, an inline card header combining the icon and specialist tag/title, followed by plain-language description, turnaround time badge, and a clear button-styled WhatsApp inquiry link).
3. **Instant Diagnostic Cost & Feasibility Estimator (`section#estimator.estimator-panel`):**
   - Guided 3-step form grid (`.calc-grid`) with fully localized `<label>` and `<option>` items in both Bengali (`bn`) and English (`en`):
     - Step 1: `select#calc-brand` (Platform: Apple / Android)
     - Step 2: `select#calc-issue` (Symptom / Failure — with smart platform hints)
     - Step 3: `input#calc-model` (Optional Phone Model, e.g., `iPhone 13, Note 12…`)
     - Primary Action Button: `button#calc-btn.btn-primary` (*"Calculate Cost"* / *"খরচ হিসাব করুন"*)
   - Inline Validation & Result Card (`#calc-error` + `div#calc-result.calc-result`):
     - Polite inline guidance (`role="status"` / `aria-live="polite"`) if a required dropdown is unselected, highlighting and focusing the missing field (while preserving `alert()` compatibility if triggered programmatically).
     - Structured result card (`#calc-result-title`, `#calc-result-desc`, and `#calc-wa-btn` with high-contrast emerald green `#127838`).
4. **Contact & Shop Location Section (`section#contact.contact-section`):**
   - Clean 2-column layout (`.contact-layout`) without double-nested cards:
     - Left (`.card-pills`): 3 large, tappable contact rows (`a.card-pill`) for Official WhatsApp Desk (`+88 01834 254875`), Official Facebook Page (`facebook.com/mobile018`), and Shop Location on Google Maps (`মিতা সিনেমা হল সংলগ্ন, জেলা পরিষদ মার্কেট, বদরগঞ্জ, রংপুর`).
     - Right (`.qr-box`): Scannable WhatsApp QR code with crisp frame and offline SVG fallback.
   - Authentic Business Ethics Quote Banner (`.ethics-box`) with Hadith reference.

### 1.3 `inventory.html` — Certified Smartphone Inventory (`24+` Handsets)
1. **Catalog Header:**
   - `.hero-badges-cluster` (Motto badge + 7-Day Replacement Guarantee badge), `h1.section-title`, `p.section-subtitle` with Google Maps link.
2. **Sticky / Accessible Filter & Search Toolbar (`.inv-controls-wrapper`):**
   - `.inv-search-bar`:
     - `.search-input-wrap` with `<label for="inv-search" class="sr-only">`, `input#inv-search`, and a clear (`×`) button (`#inv-search-clear`) when text is entered.
     - `select#inv-sort.sort-dropdown` with fully localized `<option>` labels in `bn` and `en`.
   - `.brand-chips`: 9 accessible pill buttons (`button.chip-btn`, `min-height: 40px` desktop / `44px` touch target) for `All Brands`, `Xiaomi & Poco`, `Samsung`, `Realme`, `Vivo`, `Oppo`, `Infinix & Tecno`, `OnePlus`, `Motorola`.
   - `.inv-status-bar`: Live count badge (`span#inv-count.inv-count-badge`, `aria-live="polite"`) + high-contrast guarantee badge (`span.inv-guarantee-badge`).
3. **Product Grid (`div#inventory-grid.inv-grid`):**
   - Responsive grid of 24 `.inv-card` store utility cards (`content-visibility: visible` so all 24 cards render immediately with zero blank ghost boxes).
   - Verified, working smartphone product images for all 24 handsets (fixing the 4 broken GSMArena URLs so zero `ERR_BLOCKED_BY_ORB` errors occur).
   - Friendly Empty State with a one-click **"Show All Phones / সব ফোন দেখুন"** reset button (`#inv-reset-btn`).

### 1.4 `404.html` — Bilingual Error Recovery Page
- Loads `script.js` so `data-theme` and `me_lang` (`bn` / `en`) work seamlessly.
- Full `data-i18n` attributes on the heading, description, and recovery CTAs (`Home` and `Inventory`).

---

## 2. Navigation Model
- **5 Primary Items:** `Home` (`#hero`), `Diagnostics` (`#services`), `Estimator` (`#estimator`), `Contact` (`#contact`), `Inventory 24+` (`inventory.html`).
- **Always-Visible Location:** Sliding `.nav-pill-indicator` and `.active` link state updated via scroll-spy on `index.html` and route state on `inventory.html`.
- **One Obvious Primary Action Per Screen:**
  - Hero: `Buy / Exchange Phones (24+)` (`a.btn-primary`)
  - Estimator: `Calculate` (`#calc-btn`) -> `Confirm on WhatsApp` (`#calc-wa-btn`)
  - Inventory Card: `Order Now` / `অর্ডার করুন` (`a.btn-primary.btn-full`)

---

## 3. Component Inventory (Design Tokens)
| Component | Selector | Radius | Height / Padding | Key Token Rules |
|---|---|---|---|---|
| **Primary Button** | `.btn-primary` | `--radius-pill` (`9999px`) | `min-height: 46px`, `12px 24px` | Fill `--red-main`, text `#ffffff` (6.1:1 contrast), active `scale(0.98)` |
| **Secondary Button** | `.btn-secondary` | `--radius-pill` (`9999px`) | `min-height: 46px`, `12px 24px` | Fill `--bg-surface-subtle`, border `1px solid --border-hairline`, text `--text-primary` |
| **WhatsApp Support CTA** | `.btn-live-support` | `--radius-pill` (`9999px`) | `min-height: 40px`, `8px 18px` | Fill `--green-wa` (`#127838`), text `#ffffff` (5.6:1 contrast) |
| **Segmented Toggle** | `.segmented-toggle` | `--radius-pill` (`9999px`) | `width: 76px; height: 40px` | Accessible touch size, crisp sliding thumb (`200ms cubic-bezier(0.22, 1, 0.36, 1)`) |
| **Form Select / Input** | `.form-control`, `#inv-search`, `.sort-dropdown` | `--radius-md` (`12px`) / `--radius-pill` | `min-height: 48px`, `12px 16px` | Explicit `background-color` & `color`, `2px solid --red-main` focus ring |
| **Store Utility Card** | `.service-card`, `.inv-card` | `--radius-lg` (`18px`) | `padding: 24px` | Fill `--bg-surface`, `1px solid --border-hairline`, neutral `--shadow-card` |
| **Filter Chip** | `.chip-btn` | `--radius-pill` (`9999px`) | `min-height: 40px`, `8px 18px` | Inactive: `--bg-surface`, `--text-secondary`; Active: `--red-main`, `#ffffff` |
| **Empty / Feedback State** | `.empty-state-box`, `.calc-feedback` | `--radius-lg` (`18px`) | `padding: 40px 24px` | Clear icon, plain explanation, actionable recovery button |

---

## 4. Redesigned Transitions & Motion Rules
- **Timing & Easing:** `150ms–250ms` using exponential ease-out `cubic-bezier(0.22, 1, 0.36, 1)`.
- **Explicit Property Transitions:** Never `transition: all`; explicitly transition `background-color`, `border-color`, `color`, `transform`, `box-shadow`, `opacity`.
- **Reduced Motion:** `@media (prefers-reduced-motion: reduce)` disables all non-essential transforms, smooth scroll behavior, and parallax movement while preserving instant state highlights.

---

## 5. Element & Coupling Hook Mapping Table

| Old Element / Hook | New Element / Hook | Coupling Status |
|---|---|---|
| `header.glass-header` / `.nav-container` | `header.glass-header` / `.nav-container` | **100% Preserved** |
| `.nav-links`, `.nav-pill-indicator`, `a.active` | `.nav-links`, `.nav-pill-indicator`, `a.active` | **100% Preserved** |
| `#themeToggleBtn`, `.theme-segmented-toggle` | `#themeToggleBtn`, `.theme-segmented-toggle` | **100% Preserved** |
| `#langToggleBtn`, `.lang-segmented-toggle` | `#langToggleBtn`, `.lang-segmented-toggle` | **100% Preserved** |
| `#menu-toggle`, `#mobile-drawer`, `#drawer-overlay`, `#drawer-close`, `.drawer-links` | `#menu-toggle`, `#mobile-drawer`, `#drawer-overlay`, `#drawer-close`, `.drawer-links` | **100% Preserved** |
| `section#hero`, `section#services`, `section#estimator`, `section#contact` | `section#hero`, `section#services`, `section#estimator`, `section#contact` | **100% Preserved** |
| `#calc-brand`, `#calc-issue`, `#calc-model`, `#calc-btn`, `#calc-result`, `#calc-result-title`, `#calc-result-desc`, `#calc-wa-btn` | `#calc-brand`, `#calc-issue`, `#calc-model`, `#calc-btn`, `#calc-result`, `#calc-result-title`, `#calc-result-desc`, `#calc-wa-btn` | **100% Preserved + Enhanced (bilingual options + inline feedback)** |
| `#inv-search`, `#inv-sort`, `.chip-btn[data-filter]`, `#inv-count`, `#inventory-grid` | `#inv-search`, `#inv-sort`, `.chip-btn[data-filter]`, `#inv-count`, `#inventory-grid` | **100% Preserved + Enhanced (clear search + empty reset + fixed images)** |
| `localStorage` (`me_theme`, `me_lang`), `window.reRenderInventory`, `window.refreshNavPill` | `localStorage` (`me_theme`, `me_lang`), `window.reRenderInventory`, `window.refreshNavPill` | **100% Preserved** |

---

## 6. Incremental Implementation & Commit Order (Phase 5)
1. **Increment 1:** Shared Design System Tokens & Core Stylesheet (`style.css`) + Bilingual Engine & Image Fixes (`script.js`).
2. **Increment 2:** Home Page (`index.html`) & 404 Page (`404.html`) markup, accessibility, and bilingual form controls.
3. **Increment 3:** Inventory Page (`inventory.html`) markup, search/filter ergonomics, and Service Worker cache update (`sw.js`).
4. **Increment 4:** Comprehensive Playwright E2E Verification (`tests/e2e/`), visual inspection across `360`, `390`, `768`, `820`, `1024`, `1440`, `1920` widths, Impeccable detector zero-warning check, and final documentation (`docs/CHANGELOG.md`, `docs/FOUND_ISSUES.md`, `docs/REPORT.md`).
