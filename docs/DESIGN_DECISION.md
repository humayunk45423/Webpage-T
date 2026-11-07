# Design Direction & System Decision (`docs/DESIGN_DECISION.md`)

## 1. Site Classification & Design Personality
Based on `docs/SITE_PROFILE.md`, **Mobile Express** is a dual-purpose **Local Precision Service Lab (Apple iCloud & Smartphone Diagnostics)** and **Certified Smartphone Store (`24+` Handset Catalog)** serving customers in Badarganj, Rangpur, Bangladesh.

- **Primary Surface Mode (`index.html`):** **Persuade + Operate** (Hero, Diagnostic Services, Interactive Cost & Feasibility Estimator, Direct Contact & Location).
- **Catalog Surface Mode (`inventory.html`):** **Operate + Store** (Search, Brand Chip Filtering, Price/Name Sorting, 24+ Product Cards with 1-Click WhatsApp Ordering).
- **Chosen Design Personality:**
  - **Trust, Clarity & Precision:** High-contrast typography, clean surface hierarchy, zero decorative clutter, immediate price transparency, and unmistakable primary actions for non-technical users in both Bengali (`bn`) and English (`en`).

---

## 2. Chosen Brand Design System (`./DESIGN.md`)
- **Selected System:** **Apple (`apple/DESIGN.md` from `voltagent/awesome-design-md`)**, copied to `./DESIGN.md`.
- **Why Apple's Design System Fits Mobile Express:**
  1. **Direct Domain Alignment:** Mobile Express's flagship identity is *"Apple Expert Tanvir Iqbal • Mobile Express"* and *"Apple iCloud Lab (Create, Fix & Bypass)"* alongside a 24+ smartphone retail showroom.
  2. **Product-First Showroom & Store Utility Cards:** Apple's design language pairs clean, high-trust alternating surfaces (`#ffffff` Pure White canvas and `#f5f5f7` Parchment in Light mode; `#000000`, `#161618`, and `#1d1d1f` in Dark mode) with `18px` radius (`{rounded.lg}`) store utility cards, `1px solid` hairline borders (`#e0e0e0` light / `#2c2c2e` dark), and `9999px` (`{rounded.pill}`) action pills.
  3. **Eliminates Every Baseline Anti-Pattern:** Replaces the baseline's 3D neon-red diagonal ribbons, two-axis grid overlay, colored glow shadows, gradient text, side-tab borders, and nested glass cards with calm, authoritative surfaces where the phones, prices, and diagnostic tools stand out effortlessly.

---

## 3. Brand Identity Preservation & Token Calibration
Per Phase 3 Rule 5 (*"Preserve brand identity assets that must remain (logo, name, brand colors if the owner clearly depends on them) unless they are the problem; if you change them, state why"*):
- **Preserved Brand Assets:**
  - `Mobile Express.svg` and `assets/logo.png` (crimson, black, and white emblem).
  - Brand Name (`Mobile Express` / `মোবাইল এক্সপ্রেস`), Proprietor (`Tanvir Iqbal` / `তানভীর ইকবাল`), Motto (`Buy • Exchange • Sell` / `ক্রয় • বিনিময় • বিক্রয়`), and Hadith Ethics quote (`[Sunan At-Tirmidhi, Hadith No. 1209]`).
  - **Brand Crimson Accent (`--red-main`):** Preserved from the owner's physical business card and logo, calibrated for strict **WCAG AA contrast**:
    - Light mode primary crimson: `#c8102e` (hover `#a60b24`) -> **6.1:1 contrast** against `#ffffff` white text!
    - Badge / subtle crimson text on light surface: `#9e0b22` on `#fef2f3` -> **7.8:1 contrast** (fixes baseline's 3.4:1 contrast failure).
  - **WhatsApp Action Green (`--green-wa`):**
    - Baseline used `#ffffff` text on `#25d366` which failed WCAG AA at **2.0:1**.
    - Redesigned to deep emerald `#127838` (hover `#0e5f2c`) with `#ffffff` text -> **5.6:1 WCAG AA contrast**, and `#0f6830` text on `#ecfdf3` tint badge -> **6.8:1 contrast**!

### Master Token Law (`style.css` mapped from `./DESIGN.md`)
| Token Category | Token Name | Light Mode Value | Dark Mode Value | Purpose |
|---|---|---|---|---|
| **Canvas & Surfaces** | `--bg-canvas` / `--bg-dark` | `#f5f5f7` (Apple Parchment) | `#0a0a0c` (Deep Carbon) | Page background |
| | `--bg-surface` / `--bg-panel` | `#ffffff` (Pure White) | `#141417` (Tile Surface 1) | Section & primary card surface |
| | `--bg-surface-subtle` | `#fafafc` (Pearl) | `#1c1c21` (Tile Surface 2) | Secondary surface, inputs, pills |
| | `--bg-header` | `rgba(255, 255, 255, 0.86)` | `rgba(20, 20, 23, 0.86)` | Sticky frosted header (`saturate(180%) blur(20px)`) |
| **Typography & Ink** | `--text-primary` | `#1d1d1f` (Apple Ink) | `#f5f5f7` (Off-White Ink) | Headings, body strong, prices |
| | `--text-secondary` | `#424245` (7.5:1 contrast) | `#b8b8bf` (8.2:1 contrast) | Body paragraphs, specs, subtitles |
| | `--text-dim` | `#58585d` (5.6:1 contrast) | `#94949e` (5.3:1 contrast) | Captions, metadata, placeholders |
| **Borders & Dividers** | `--border-hairline` | `#e0e0e5` | `#2c2c32` | 1px card & control borders |
| | `--border-strong` | `#c7c7cc` | `#3d3d45` | Hover & active control borders |
| **Brand & Semantic** | `--red-main` | `#c8102e` | `#e11d38` | Primary brand action & active tab accent |
| | `--red-hover` | `#a60b24` | `#f43f5e` | Primary button hover / dark mode highlight |
| | `--red-subtle` | `#fef2f3` | `rgba(225, 29, 56, 0.14)` | Subtle tint surface |
| | `--red-text-accent` | `#9e0b22` | `#fda4af` | High-contrast crimson text on light/dark |
| | `--green-wa` | `#127838` | `#15803d` | Accessible WhatsApp CTA fill (5.6:1 with `#fff`) |
| | `--green-text` | `#0f6830` | `#4ade80` | Accessible guarantee badge text |
| **Typography Faces** | `--font-main` | `'Public Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` | Same | Clean, high-legibility humanist/geometric sans |
| | `--font-bengali` | `'Noto Sans Bengali', 'Anek Bangla', sans-serif` | Same | Authentic, crisp Bengali script rendering |
| **Radii (`DESIGN.md`)** | `--radius-sm` / `md` / `lg` / `pill` | `8px` / `12px` / `18px` / `9999px` | Same | Apple shape grammar |
| **Elevation** | `--shadow-card` | `0 4px 16px rgba(0, 0, 0, 0.04)` | `0 6px 20px rgba(0, 0, 0, 0.35)` | Neutral, soft offset elevation (zero colored glow) |

---

## 4. Taste Skill Calibration (`BOLD` / `MOTION` / `DENSITY`)
- **BOLD: Moderate (6/10)** — Confident typographic hierarchy (`52px` desktop hero display, `34px` section headings, `22px` clear BDT prices) and unmistakable primary action buttons without visual noise or neon gimmicks.
- **MOTION: Restrained (3/10)** — Purposeful `150–250ms` exponential ease-out (`cubic-bezier(0.22, 1, 0.36, 1)`) micro-interactions on hover/press (`scale(0.98)` press feedback, `-2px` card hover lift, smooth nav pill glide); zero infinite pulsing dots, zero bounce easing, and full `prefers-reduced-motion: reduce` support.
- **DENSITY: Comfortable (5/10)** — Generous breathing room (`24px` card padding, `64px–80px` section rhythm, `16px–17px` body copy at `1.55` line-height) so non-technical users in Bengali or English can scan services, calculate repair costs, and compare smartphones without feeling overwhelmed.

---

## 5. Impeccable Baseline Critique & Polish Plan
1. **Eliminate all 47 baseline detector warnings/errors:**
   - Remove `.pulse-indicator` infinite animation (`pulsing-dot` error).
   - Replace `.red-gradient-text` with solid high-contrast typography (`gradient-text` warning).
   - Remove `border-left: 4px` side-tab on `#calc-result` (`side-tab` warning) and replace with a clean structured result card with step-by-step cost/time breakdown.
   - Replace stacked `.s-icon-box` tiles above `<h3>` (`icon-tile-stack` warning) with an inline header row (`icon + badge/title`) inside each service card.
   - Remove colored glow shadows (`dark-glow` warning), `.grid-texture` (`codex-grid-background`), and `cubic-bezier(0.34, 1.56, 0.64, 1)` (`bounce-easing`).
   - Flatten nested cards (`nested-cards` warning): sections use clean layout wrappers instead of wrapping cards inside another `.glass-panel` card.
   - Enforce minimum `12px` (`0.75rem`) on all badges/meta labels and `16px–17px` on body text (eliminating all `undersized-ui-text` and `tiny-text` warnings).
   - Replace `Plus Jakarta Sans` with `Public Sans` + system SF Pro stack (`overused-font` warning).
2. **Fix all 4 broken GSMArena handset image URLs** so every phone in the 24-device catalog renders a crisp, verified smartphone image with zero `ERR_BLOCKED_BY_ORB` network errors.
