# Changelog - Mobile Express Web App

## [v1.2.6] - 3-Point Floating Chips Symmetry, Bengali Mobile Motto Equalization & Desktop Layout Harmony
### Changed
- **Equilateral 3-Point Floating Chips**:
  - Completely removed the 4th chip (`100% Genuine Handsets` / `১০০% অরিজিনাল ফোন`) from [index.html](file:///f:/Me%20&%20My%20Docs/1.%20Recent%20Projects/Webpage-T/index.html#L580-L596).
  - Moved the `Exchange` / `এক্সচেঞ্জ সুবিধা` pill (`.chip-2`) to the exact vertical center on the right side (`top: 50%; transform: translateY(-50%);`) on both desktop and mobile.
  - Produces an uncluttered, balanced triangular composition around the 3 phones (Top-Left: `Used • Verified`, Bottom-Left: `Repair & iCloud Unlock`, Center-Right: `Exchange`).
- **Bengali Motto & Brand Length Equalization on Mobile**:
  - Sized `.lang-bn .hero-motto` to `clamp(1.72rem, 7.7vw, 1.95rem)` with `letter-spacing: 0;` and `word-spacing: 0.05em;`.
  - "ক্রয় • বিনিময় • বিক্রয়।" now renders at the exact same collective horizontal length as "মোবাইল এক্সপ্রেস" across all mobile viewports (e.g. 288.8px vs 285.5px on 390px, a 98.8% match; 296.2px vs 296.6px on 412px, a 99.9% match).
- **Desktop Typography & Layout Spacing Harmony**:
  - Rebalanced `.hero-layout` desktop grid to `grid-template-columns: minmax(380px, 450px) 1fr; gap: 48px;`, ensuring the textual content column has ample width.
  - Refined `.hero-actions` buttons with `padding: 14px 26px; font-size: 0.98rem;` ensuring both primary and secondary action buttons sit side by side on one line (`STACKED=False`) across all desktop resolutions (1200px to 1440px+).
  - Removed negative letter-spacing for Bengali script (`letter-spacing: 0 !important;`), resolving cramped conjuncts (`যুক্তবর্ণ`).
  - Refined Bengali hero description copy to flow naturally without awkward word breaks and without repeating the motto keywords right above the buttons.

---

## [v1.2.5] - Mobile Brand Name Harmonized to Top Tablet Width
### Changed
- **Mobile Brand Name Proportional Expansion**: Sized `.hero-brand-name` on mobile viewports ($\le 768\text{px}$) to `clamp(2.15rem, 10.0vw, 2.50rem)` with `padding: 6px 2px 5px`, `line-height: 1.22`, and `letter-spacing: -0.025em`.
  - The rendered text length of "মোবাইল এক্সপ্রেস" / "Mobile Express" now precisely matches the horizontal span of the top "অ্যাপল এক্সপার্ট তানভীর ইকবাল • মোবাইল এক্সপ্রেস" tablet badge (280.1px vs 281.7px, a 99.4% horizontal match on standard 390px mobile screens).
  - Maintained zero line wrapping and zero viewport horizontal overflow (`scrollWidth == clientWidth`).
- **Motto Alignment**: Sized `.hero-motto` to `clamp(1.50rem, 6.4vw, 2.05rem)` with `line-height: 1.26` and `padding: 4px 2px 6px`, preserving balanced typographic hierarchy underneath the enlarged brand title.

---

## [v1.2.4] - White Mode Red Right Phone & White Left Screen, Battery Icon Alignment & Complete 7-Day Guarantee Removal
### Changed
- **White Mode Phone Color Refinement**:
  - Right phone back body updated to sleek Crimson / Product(RED) gradient (`url(#backPhoneGradRed)`), with matching dark crimson camera plateau (`url(#cameraPlateGradRed)`).
  - Left phone screen updated to **pure white** (`#ffffff`) with subtle dark UI placeholder bars (`#0f172a`).
  - Dark Mode preserved as before: all screens pop in high-contrast white against the dark backdrop.
- **Middle Phone Battery Icon Realignment**:
  - Repositioned cellular signal bars (`x="284..296"`) and battery gauge body (`x="304..320"`), completely resolving the previous placement where the battery nub overlapped the top-right rounded corner curve (`rx="34"`). Status bar now has $\ge 20\text{px}$ clearance from screen corner curvature.
- **Comprehensive Removal of "7-Day Guarantee / Replacement"**:
  - Removed every occurrence of 7-Day Replacement Guarantee across all files (`index.html`, `script.js`, `inventory.html`, `llms.txt`).
  - Updated SVG middle phone showcase card to "Certified Handsets In Stock / 100% Motherboard Tested".
  - Updated floating chip-4 to "100% Genuine Handsets" (`hero-chip-genuine`) with circle-check icon.
  - Updated inventory badges and subtitles to "100% Tested & Verified Handsets" (`guarantee-badge`).

---

## [v1.2.3] - Restored Comfortably Big & Impactful Typography
### Changed
- **Impactful Headline Sizing**: Scaled `.hero-title` to comfortably big, bold dimensions:
  - Mobile: `clamp(1.58rem, 6.5vw, 2.12rem)` (up from 1.35rem)
  - Desktop: `clamp(2.3rem, 3.3vw, 3.3rem)` (up from 2.05rem)
  - Delivers bold, eye-catching visual weight for both "মোবাইল এক্সপ্রেস" / "Mobile Express" and "ক্রয় • বিনিময় • বিক্রয়।" / "Buy • Exchange • Sell." without line wrapping or truncation.
- **Comfortable Badge Presence**: Scaled `.apple-specialist-badge` to `clamp(0.69rem, 2.75vw, 0.80rem)` on mobile (`padding: 5px 14px`) and `clamp(0.78rem, 1.0vw, 0.88rem)` on desktop (`padding: 6px 16px`), with an enlarged Apple icon (`0.95rem` mobile / `1.05rem` desktop), restoring a premium, official presence while strictly maintaining single-line formatting.

---

## [v1.2.2] - Resolution of Glyph Ascender/Descender Clipping
### Fixed
- **Gradient Background Bounding Box Expansion**: Resolved glyph truncation where Bengali top vowel matras (`ি`, `ী`) and English descending stems (`y`, `g`, `p`, `q`) were sliced off by `-webkit-background-clip: text`. Added `-webkit-box-decoration-break: clone`, tuned vertical padding (`padding: 4px 2px 6px`), and increased headline line-height (`1.25` on title, `1.22` on brand, `1.28` on motto). Automated pixel-level boundary analysis confirms 100% full glyph rendering with generous padding (top padding $\ge 4\text{px}$, bottom padding $\ge 11\text{px}$) across all viewports.
- **Top Badge Vertical Breathing Room**: Increased badge padding to `padding: 5px 14px` on desktop and `padding: 4px 12px` on mobile with `line-height: 1.3`, completely preventing the pill border from touching or clipping the text while maintaining strict single-line display (`white-space: nowrap !important;`).

---

## [v1.2.1] - Typography Spacing & Bilingual Harmony Fixes
### Fixed
- **Top Badge Single-Line Display**: `অ্যাপল এক্সপার্ট তানভীর ইকবাল • মোবাইল এক্সপ্রেস` and `Apple Expert Tanvir Iqbal • Mobile Express` styled with `white-space: nowrap !important;` and balanced font size (`clamp(0.55rem, 2.5vw, 0.67rem)` on mobile, `clamp(0.64rem, 0.9vw, 0.78rem)` on desktop). Full text renders on a single line on all screen sizes down to 320px with zero line breaks.
- **Dead Space Elimination**: Removed `<br>` between `.hero-brand-name` and `.hero-motto` and reduced vertical gap to a tight 3px–4px rhythm.
- **Bilingual Volume & Height Symmetry**: Standardized desktop headline font size to `clamp(2.05rem, 2.85vw, 2.85rem)` with `white-space: nowrap;` on `.hero-motto`. English ("Buy • Exchange • Sell.") and Bengali ("ক্রয় • বিনিময় • বিক্রয়।") occupy the exact same height (94.3px on desktop, 50.5px on mobile), eliminating all line wraps and awkward trailing words.

---

## [v1.2.0] - Hero Layout Inversion, Mobile Reordering & High-Contrast Theme Harmonization

### Summary
Refined the Hero visual architecture and responsive layout based on user feedback:
1. Desktop composition inverted: phone cluster is positioned on the **LEFT** side and textual content & CTAs are on the **RIGHT** side.
2. Fixed mobile horizontal overflow: eliminated unwanted viewport expansion and restored full visibility to the mobile hamburger menu toggle.
3. Title lines strictly separated: "মোবাইল এক্সপ্রেস" (brand) and "ক্রয় • বিনিময় • বিক্রয়।" (motto) display on two distinct lines across all viewports.
4. Mobile stacking reordered per exact 1–8 numbered sequence:
   - 1: Apple Expert Specialist Badge (`.hero-badges-cluster`)
   - 2 & 3: Brand Headline & Motto (`.hero-title`)
   - 4: Smartphone Stack Visual (`.hero-visual-col`)
   - 5 & 6: Action Buttons (`.hero-actions`)
   - 7: Trusted Description Paragraph with Google Maps (`.hero-desc`)
   - 8: Key Metrics Stats Row (`.hero-stats-row`)
5. High-contrast screen theme inversion:
   - **Dark Mode**: Mobiles screen background is **WHITE** so it pops vividly against the dark page background.
   - **Light Mode**: Mobiles screen background is **DARK** so it pops vividly against the light glass card background.

---

## [v1.1.0] - Hero Phone Visual Redesign (hero-phone-visual-redesign_v1)

### Summary
Redesigned the homepage Hero section so any visitor instantly recognizes Mobile Express as a used-phone sales, exchange, and repair & iCloud unlock destination in under 1 second without reading text blocks.

### Changes Implemented
1. **Desktop Two-Column Hero Composition**:
   - Modern glassmorphic hero card on desktop (`min-width: 992px`) into a balanced two-column layout.
   - Sits on top of a soft red circular ambient glow (`radial-gradient` + `filter: blur`) echoing the site's red diagonal bands.
2. **Vector Smartphone Cluster (Inline SVG)**:
   - Flagship front phone, back-view camera module phone, and diagnostic profile phone.
   - Total SVG weight < 15KB with 0 layout shift (CLS ≈ 0).
3. **Floating Glassmorphic Info Chips**:
   - 4 glass-styled pills overlapping the phone cluster with red FontAwesome icons (`hero-chip-verified`, `hero-chip-exchange`, `hero-chip-repair`, `hero-chip-warranty`).
4. **Motion, Performance & Accessibility**:
   - GPU-accelerated motion using only `transform` and `opacity`.
   - `IntersectionObserver` automatically pauses floating animations when the hero is scrolled out of view.
   - `prefers-reduced-motion: reduce` completely disables floating animations for accessibility.
