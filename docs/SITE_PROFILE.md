# Site Profile (`docs/SITE_PROFILE.md`)

## 1. Site Identity & Business Classification
- **Business Name:** Mobile Express (মোবাইল এক্সপ্রেস)
- **Proprietor / Founder:** Tanvir Iqbal (তানভীর ইকবাল) — Apple Expert & Smartphone Diagnostics Specialist
- **Motto:** Buy • Exchange • Sell (ক্রয় • বিনিময় • বিক্রয়)
- **Physical Location:** Mita Cinema Hall Adjacent, Zilla Parishad Market, Badarganj, Rangpur 5420, Bangladesh (`25.6747, 89.0198`)
- **Site Type:** Dual-surface **Local Technical Service & Diagnostics Center + Certified Smartphone Store / Catalog** (`MobilePhoneStore`, `ElectronicsRepairShop`, `LocalBusiness`)
- **Primary Audience:**
  - Local everyday smartphone owners and non-technical customers in Badarganj, Rangpur, and surrounding northern Bangladesh districts looking to buy, exchange, or sell used/certified smartphones or get locked/disabled/dead phones repaired quickly.
  - Bilingual audience: Default language is **Bengali (`bn`)**, with full **English (`en`)** toggle support.
- **Primary Business Goal:** Drive high-intent customer inquiries and store visits via **WhatsApp Live Support** (`+8801834254875`) and **Google Maps directions**, while establishing immediate trust through transparent diagnostic pricing/time estimates, a 7-Day Replacement Guarantee, and authentic business ethics.

## 2. Top 3 User Tasks
1. **Check Diagnostic & Repair Feasibility + Cost Estimate (`index.html#services` & `index.html#estimator`):**
   - Users with locked iPhones (iCloud Activation Lock, Disabled/Unavailable screen, Baseband/Unable to Activate), locked Androids (Google FRP lock, SIM/Carrier lock), or bricked phones (Dead Boot / Qualcomm 9008 / Motherboard short) select their platform and issue in the **Instant Diagnostic Estimator**, see the exact time and BDT (`৳`) cost range in Bengali or English, and click **Confirm on WhatsApp** with a pre-filled diagnostic consultation message.
2. **Browse, Filter, Search & Order Certified Smartphones (`inventory.html`):**
   - Users looking to buy or exchange a smartphone browse 24+ motherboard-tested devices (Xiaomi, Poco, Realme, Samsung, Vivo, Oppo, Infinix, Tecno, OnePlus, Motorola), filter by brand chip, search by model/camera/processor (e.g., `Note 13`, `108MP`, `G99`), sort by price or name, and click **Order Now / অর্ডার করুন** to open a pre-filled WhatsApp message containing the exact handset name and price.
3. **Contact the Shop / Get Directions (`index.html#contact` & Header/Floating WhatsApp):**
   - Users connect directly via WhatsApp (`+8801834254875` or QR code scan), visit the Official Facebook Page (`facebook.com/mobile018`), or open the exact shop location on Google Maps (`Mita Cinema Hall Adjacent, Zilla Parishad Market, Badarganj, Rangpur`).

## 3. Technology Stack
- **Architecture:** Multi-page static web application (MPA) with Progressive Web App (PWA) offline support.
- **Markup:** Semantic HTML5 (`index.html`, `inventory.html`, `404.html`) with comprehensive SEO meta tags, OpenGraph, Twitter Cards, Geo tags, and JSON-LD structured data (`MobilePhoneStore`, `ElectronicsRepairShop`, `LocalBusiness`, `CollectionPage`, `BreadcrumbList`).
- **Styling:** Vanilla CSS3 (`style.css`, 2,492 lines) using CSS custom properties (`:root` and `[data-theme="light"]`), Flexbox, CSS Grid, responsive media queries, and glassmorphism/3D ribbon layers.
- **Scripting:** Vanilla ES6+ JavaScript (`script.js`, 882 lines), zero external JS runtime dependencies.
- **Typography:** Google Fonts:
  - English: `Plus Jakarta Sans` (weights 400–900)
  - Bengali: `Noto Sans Bengali` (weights 400–900) & `Anek Bangla` (weights 400–800)
- **Icons:** Font Awesome 6.5.0 (`https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css`).
- **Assets & External APIs:**
  - Brand logos: `Mobile Express.svg`, `assets/logo.png`, `assets/logo.svg`
  - QR Code API: `https://api.qrserver.com/v1/create-qr-code/?size=160x160&data=https%3A%2F%2Fwa.me%2F8801834254875...`
  - Handset Catalog Images: GSMArena CDN (`https://fdn2.gsmarena.com/vv/bigpic/...`) with automatic `onerror` fallback to `Mobile Express.svg`
  - Messaging Integration: WhatsApp `https://wa.me/8801834254875?text=...`
- **Client Storage:**
  - `localStorage.getItem('me_theme')` / `localStorage.setItem('me_theme', ...)` (`'light'` default, `'dark'`)
  - `localStorage.getItem('me_lang')` / `localStorage.setItem('me_lang', ...)` (`'bn'` default, `'en'`)
  - Cache Storage API via Service Worker (`sw.js`, cache name `mobile-express-v1.0.0`, Stale-While-Revalidate strategy).
- **Hosting / Deployment:** Vercel (`https://mobileexpress.vercel.app/`), with `robots.txt`, `sitemap.xml`, `llms.txt`, and `manifest.json`.

## 4. Languages, Direction & Responsive Breakpoints
- **Languages:** Bilingual **Bengali (`bn`, default)** and **English (`en`)**, both LTR (`dir="ltr"`).
- **Numeral Localization:** Dynamic conversion of Arabic digits (`0-9`) to Bengali digits (`০-৯`) via `toBengaliDigits()` when `bn` is active.
- **Responsive Breakpoints Currently in Use (`style.css`):**
  - Desktop: `> 960px` (max-width containers `1160px` nav / `1200px` main content)
  - Tablet / Mobile Nav Collapse: `@media (max-width: 960px)` (collapses top `.nav-links`, `.btn-live-support`, and header `.segmented-toggle` into `#menu-toggle` hamburger + `#mobile-drawer`)
  - Mobile Compact Layout: `@media (max-width: 640px)` (single-column services/estimator, 2-column compact inventory grid, horizontal scrolling `.brand-chips`)
  - Ultra-Narrow Fallback: `@media (max-width: 339px)` (1-column inventory grid)
