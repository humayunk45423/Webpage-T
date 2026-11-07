# Baseline Interaction & Transition Log (`docs/INTERACTION_AND_TRANSITION_LOG.md`)

Recorded on the original baseline site (`baseline-before-redesign`) running at `http://127.0.0.1:8123` inside real headless Chromium via Playwright across Desktop (`1440×900`), Tablet (`820×1180`), and Mobile (`390×844`).

## 1. Baseline Screenshots Captured (`tests/baseline/`)
1. `tests/baseline/index_desktop_1440_light_bn.png` — Home page, 1440px, Light mode, Bengali (default)
2. `tests/baseline/index_desktop_1440_light_en.png` — Home page, 1440px, Light mode, English
3. `tests/baseline/index_desktop_1440_dark_en.png` — Home page, 1440px, Dark mode, English
4. `tests/baseline/index_desktop_1440_estimator_result.png` — Estimator section after calculating `Apple` + `iCloud Activation Lock`
5. `tests/baseline/inventory_desktop_1440_light_bn.png` — Inventory page, 1440px, Light mode, Bengali (shows `content-visibility: auto` blank cards bug on cards 13–24 and 4 ORB fallback logos)
6. `tests/baseline/inventory_desktop_1440_filter_samsung.png` — Inventory page filtered by `Samsung` (4 handsets)
7. `tests/baseline/inventory_desktop_1440_empty_state.png` — Inventory page empty search result (`nonexistentphone123`)
8. `tests/baseline/404_desktop_1440.png` — 404 page, 1440px
9. `tests/baseline/index_tablet_820_light_bn.png` — Home page, 820px Tablet
10. `tests/baseline/inventory_tablet_820_light_bn.png` — Inventory page, 820px Tablet
11. `tests/baseline/404_tablet_820.png` — 404 page, 820px Tablet
12. `tests/baseline/index_mobile_390_light_bn.png` — Home page, 390px Mobile
13. `tests/baseline/index_mobile_390_drawer_open.png` — Home page, 390px Mobile with navigation drawer open
14. `tests/baseline/inventory_mobile_390_light_bn.png` — Inventory page, 390px Mobile (2-column compact grid)
15. `tests/baseline/404_mobile_390.png` — 404 page, 390px Mobile

---

## 2. Step-by-Step Interaction & Transition Log

### Interaction 1: Theme Toggle (`#themeToggleBtn` / `.theme-segmented-toggle`)
- **Before-state:** `<html lang="bn" class="lang-bn" data-theme="light">`, `#themeToggleBtn[data-state="left"]`, `.toggle-slider` at `translateX(0)`.
- **Action:** Click `#themeToggleBtn`.
- **After-state:** `<html data-theme="dark">`, `#themeToggleBtn[data-state="right"]`, `localStorage.getItem('me_theme') === 'dark'`.
- **Animation:**
  - `.toggle-slider`: `transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), background-color 0.25s ease, box-shadow 0.25s ease`
  - `body`: `background-color 0.28s cubic-bezier(0.16, 1, 0.3, 1), color 0.28s cubic-bezier(0.16, 1, 0.3, 1)`

### Interaction 2: Language Toggle (`#langToggleBtn` / `.lang-segmented-toggle`)
- **Before-state:** `body.lang-bn`, `#langToggleBtn[data-state="left"]`, `currentLanguage = 'bn'`, hero title = `মোবাইল এক্সপ্রেস / ক্রয় • বিনিময় • বিক্রয়।`.
- **Action:** Click `#langToggleBtn`.
- **After-state:** `body` removes `lang-bn`, `#langToggleBtn[data-state="right"]`, `localStorage.getItem('me_lang') === 'en'`, hero title = `Mobile Express / Buy • Exchange • Sell.`. On `inventory.html`, prices change from `৳ ২২,৯৯৯` to `৳ 22,999` and count changes from `২৪ টি হ্যান্ডসেট স্টকে রয়েছে` to `24 Handsets Available`.
- **Animation:**
  - `.toggle-slider`: `transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1)`
  - `.nav-pill-indicator`: repositioned via `window.refreshNavPill()` after `50ms` timeout (`transition: none` during resize recalc).

### Interaction 3: Top Navigation Pill & Smooth Scroll (`.nav-links a`)
- **Before-state:** `a[href="#hero"]` has `.active`; `.nav-pill-indicator` positioned over `Home` (`হোম`).
- **Action:** Click `a[href="#estimator"]` (or scroll down to `#estimator`).
- **After-state:** `a[href="#estimator"]` has `.active`; `window.location.hash === '#estimator'`; viewport smoothly scrolled to `#estimator.offsetTop - 105`.
- **Animation:**
  - `.nav-pill-indicator`: `transform 0.35s cubic-bezier(0.25, 1, 0.35, 1), width 0.35s cubic-bezier(0.25, 1, 0.35, 1), opacity 0.2s ease`
  - Window scroll: native `behavior: 'smooth'`.

### Interaction 4: Mobile Navigation Drawer (`#menu-toggle` / `#drawer-close` / `#drawer-overlay`)
- **Before-state:** `#mobile-drawer` at `right: -100%`, `#drawer-overlay` at `opacity: 0; pointer-events: none`, `body.style.overflow = ''`.
- **Action:** Click `#menu-toggle` (at 390px or 820px viewport).
- **After-state:** `#mobile-drawer.open` (`right: 0`), `#drawer-overlay.active` (`opacity: 1; pointer-events: auto`), `body.style.overflow = 'hidden'`.
- **Animation:**
  - `#mobile-drawer`: `right 0.35s cubic-bezier(0.16, 1, 0.3, 1)`
  - `#drawer-overlay`: `opacity 0.3s ease`

### Interaction 5: Diagnostic Cost & Feasibility Calculator (`#estimator`)
- **Before-state:** `#calc-brand` value `""`, `#calc-issue` value `""`, `#calc-result` has `display: none` (no `.visible` class).
- **Action:** Select `#calc-brand = "apple"`, `#calc-issue = "icloud"`, fill `#calc-model = "iPhone 13 Pro"`, click `#calc-btn`.
- **After-state:** `#calc-result.visible` (`display: flex`), `#calc-result-title` = `Apple iCloud Activation Lock Resolution (15 - 45 Mins)` (or Bengali equivalent), `#calc-result-desc` = `Diagnostic Cost Range: ৳ 1,500 - ৳ 4,500...`, `#calc-wa-btn` `href` updated to `https://wa.me/8801834254875?text=...`.
- **Animation:** Instant `display: flex` + `resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' })`.

### Interaction 6: Inventory Brand Filtering, Live Search & Sorting (`inventory.html`)
- **Before-state:** `.chip-btn[data-filter="all"]` is `.active`, `#inv-count` = `২৪ টি হ্যান্ডসেট স্টকে রয়েছে`, 24 `.inv-card` elements in `#inventory-grid`.
- **Action A:** Click `.chip-btn[data-filter="samsung"]`.
- **After-state A:** `.chip-btn[data-filter="samsung"]` is `.active`, `#inv-count` = `৪ টি হ্যান্ডসেট স্টকে রয়েছে`, 4 Samsung cards rendered.
- **Action B:** Select `#inv-sort = "price-low"`.
- **After-state B:** Cards re-ordered ascending by price (`Galaxy A04s` ৳13,500 -> `Galaxy A14` ৳18,500 -> `Galaxy M14 5G` ৳21,000 -> `Galaxy A24` ৳24,500).
- **Action C:** Type `"nonexistentphone123"` into `#inv-search`.
- **After-state C:** `#inv-count` = `০ টি হ্যান্ডসেট স্টকে রয়েছে`, `#inventory-grid` displays empty state message (`কোনো হ্যান্ডসেট পাওয়া যায়নি`).
- **Animation:** `.chip-btn` transition `all 0.16s ease`; `.inv-card` hover `all 0.28s cubic-bezier(0.16, 1, 0.3, 1)`.

---

## 3. Baseline Console & Network Summary
- **Console Errors:** `0`
- **Console Warnings:** `0`
- **Failed Network Requests at Baseline:** 4 GSMArena image URLs blocked by `net::ERR_BLOCKED_BY_ORB` (`xiaomi-redmi-note-12.jpg`, `realme-10-4g.jpg`, `samsung-galaxy-a24-4g.jpg`, `samsung-galaxy-m14-5g.jpg`).
