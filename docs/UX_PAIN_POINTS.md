# UX Pain Points & Accessibility Audit (`docs/UX_PAIN_POINTS.md`)

A comprehensive audit of everything a non-technical customer in Badarganj, Rangpur (or first-time visitor) struggles with on the baseline site.

## 1. Language Mixing & Untranslated Controls (High Cognitive Load for Bengali Users)
- **The Problem:** Although the site defaults to Bengali (`bn`) for local customers in Badarganj, Rangpur, the most important interactive form on the home page (**Instant Diagnostic Estimator**) has **English-only dropdown options** (`Select Platform...`, `Apple (iPhone / iPad)`, `iCloud Activation Lock`, `Unable to Activate / Baseband`, `Dead Boot / Qualcomm 9008`, `Motherboard Power Short`) and an English-only WhatsApp confirmation button (`Confirm on WhatsApp`).
- **On `inventory.html`:** The sort dropdown (`Sort: Featured`, `Price: Low to High`, `Price: High to Low`, `Name: A to Z`) is also English-only even in Bengali mode.
- **On `404.html`:** The heading and buttons are hardcoded in Bengali, the paragraph is hardcoded in English, and `script.js` is not loaded at all.
- **Grandma-Proof Fix:** Localize 100% of `<select>` options, placeholders, buttons, helper hints, and `404.html` in `I18N_DICTIONARY` (`bn` and `en`), using plain, everyday terms alongside technical names (e.g., `আইক্লাউড লক (iCloud Lock)`, `ফোন চালু হচ্ছে না (Dead Boot)`).

## 2. Technical Jargon Without Plain-Language Context
- **The Problem:** Terms like *"Proprietary diagnostic algorithms"*, *"Ramdisk activation lock bypass"*, *"Qualcomm 9008 EDL revival"*, *"Direct ISP memory reconstruction"*, *"Establish Connection"*, and *"Acquire Device"* sound like sci-fi/cybersecurity jargon rather than a friendly, trustworthy neighborhood smartphone shop and repair center.
- **The Estimator Problem:** If a user selects `Apple (iPhone / iPad)` in `#calc-brand`, the `#calc-issue` dropdown still displays Android-only options (`Android Google FRP Lock`, `Dead Boot / Qualcomm 9008`), and vice versa.
- **Grandma-Proof Fix:**
  - Keep all technical keywords intact for SEO and power users, but clarify headings, descriptions, and button labels so a non-technical person immediately understands what each service fixes.
  - Dynamically filter or clearly label `#calc-issue` options based on the selected platform (while keeping all option values available for direct programmatic selection), and include the user's typed `#calc-model` in the calculation summary and WhatsApp message!

## 3. Hostile `window.alert()` Error & Missing Inline Form Feedback
- **The Problem:** Clicking `#calc-btn` without selecting Platform or Issue triggers a blocking browser `window.alert()` with no visual indication on the form of which dropdown was missed.
- **Grandma-Proof Fix:** Highlight the unselected field(s), focus the first missing input, and display a polite inline status/error message (`role="alert"` / `aria-live="polite"`) right below the form that tells the user exactly what to pick next—while also automatically updating the estimate whenever the user changes Platform, Issue, or Model after first calculation.

## 4. Hidden Language Switch & Support Action on Mobile (`<= 960px`)
- **The Problem:** On mobile phones (`390px` / `360px`—where >85% of local customers browse), the top header hides both the `BN / EN` language switch and the `Theme` switch inside the hamburger drawer, leaving only a small `36×36px` hamburger icon. Worse, the floating green WhatsApp circle overlaps right on top of page content (`index_mobile_390_light_bn.png` shows it covering the first service card's badge and heading).
- **Grandma-Proof Fix:**
  - Keep a compact, touch-friendly language toggle (`বাং / EN`) and theme button accessible, and ensure `#menu-toggle` is at least `44×44px`.
  - Give `.floating-wa-btn` safe bottom/right clearance and a clear label or non-overlapping dock so it never obscures text or badges.

## 5. Blank Ghost Cards & Broken Phone Thumbnails on `inventory.html`
- **The Problem:**
  1. `content-visibility: auto` on `.inv-card` causes below-the-fold cards to appear blank until scrolled.
  2. Four GSMArena image URLs (`Redmi Note 12`, `Realme 10`, `Galaxy A24`, `Galaxy M14 5G`) are blocked by browser ORB (`net::ERR_BLOCKED_BY_ORB`) and fall back to the square red-and-black shop logo (`Mobile Express.svg`), making those 4 phones look like missing/broken listings compared to the other 20 phones.
  3. When a search + brand filter combination yields 0 results, there is no button to reset the search/filter—a non-technical user has to manually backspace the search box and scroll the chip bar back to "All Brands".
- **Grandma-Proof Fix:**
  1. Remove `content-visibility: auto` from `.inv-card` (24 cards is small and renders in <2ms without blank-card artifacts).
  2. Provide clean, reliable fallback/local SVG device renders or verified working product images so every single handset card displays a crisp smartphone illustration/photo with zero `ERR_BLOCKED_BY_ORB` network errors.
  3. Add a prominent **"Show All Phones / সব ফোন দেখুন"** reset button inside the empty state AND a clear search (`×`) button inside the search bar.

## 6. Accessibility Floor Violations (WCAG AA & Vercel Guidelines)
- **Zero Keyboard Focus Indicators:** `style.css:134-140` sets `outline: none !important; box-shadow: none;` on `button:focus-visible` and `a:focus-visible`, making keyboard navigation impossible to track.
- **Severe Contrast Failures:**
  - White text `#ffffff` on bright green `#25d366` (`.btn-live-support`, `#calc-wa-btn`) is **2.0:1** (fails WCAG AA 4.5:1).
  - Green text `#25d366` on white background (`.inv-guarantee-badge`) is **2.0:1**.
  - Light red text `#ef233c` on pale pink `#fbebee` badges is **3.4:1 – 3.7:1**.
- **Tiny Text on Mobile:** Mobile inventory card specs (`9.9px`), badges (`8.6px`), and stat labels (`9.3px`) are far below the 11px–16px readability floor.
- **No `prefers-reduced-motion` Support:** Continuous `.pulse-indicator` animation, spinning badge icon (`rotateSlow`), and scroll parallax run unconditionally even when `prefers-reduced-motion: reduce` is enabled.
- **Visual Clutter / AI-Slop:** Heavy diagonal 3D red ribbons, two-axis grid overlay, red neon glow shadows, gradient text, and nested glass cards reduce legibility and make the page feel like a generic template rather than a trustworthy precision hardware lab and retail store.
