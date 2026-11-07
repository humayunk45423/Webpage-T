# Project Run & Build Guide (`docs/RUN.md`)

## Overview
**Mobile Express** (`https://mobileexpress.vercel.app/`) is a zero-build static web application (HTML5, CSS3, Vanilla ES6+ JavaScript, Progressive Web App Service Worker) serving a dual-purpose local business in Badarganj, Rangpur, Bangladesh:
1. **Smartphone Diagnostics & Repair Lab** (Apple iCloud unlock/bypass/account creation, Android FRP removal, Dead Boot & Motherboard repair, Carrier unlock) with an interactive Diagnostic Cost & Feasibility Estimator.
2. **Certified Smartphone Inventory Catalog** (`inventory.html`) featuring 24+ tested devices with live search, brand filtering, price/name sorting, and direct WhatsApp ordering.

---

## Prerequisites
- **Python 3.12+** (installed at `C:\Users\Humayoun\AppData\Local\Programs\Python\Python312\python.exe`)
- **Playwright (Python & CLI v1.64.1)** with Chromium installed (`playwright install chromium`)
- **Deno 2.9.7+** (installed via WinGet, provides `deno` and `node` compatibility layer)

---

## Commands

### 1. Install Dependencies
No build-step dependencies are required for the static production bundle.
For E2E verification with Playwright:
```powershell
playwright install chromium
```

### 2. Run Local Development / Preview Server
Serve the project root over HTTP on port `8123` (or `8080`):
```powershell
python -m http.server 8123 --bind 127.0.0.1
```
Then open:
- Home / Diagnostics & Estimator: `http://127.0.0.1:8123/index.html`
- Smartphone Inventory Catalog: `http://127.0.0.1:8123/inventory.html`
- 404 Error Page: `http://127.0.0.1:8123/404.html`

### 3. Build Verification
Since the site is deployed directly as static assets (Vercel / Cloudflare Workers static), build verification checks:
- Valid HTML5 markup across `index.html`, `inventory.html`, `404.html`
- Valid JavaScript syntax in `script.js` and `sw.js`
- Valid JSON in `manifest.json` and embedded `application/ld+json` schemas
- Impeccable deterministic detector scan:
  ```powershell
  .\.agents\skills\impeccable\scripts\impeccable.cmd detect --json index.html inventory.html 404.html
  ```

### 4. Run End-to-End Playwright Test Suite
Run the automated Playwright test suite in `tests/e2e/`:
```powershell
python tests/e2e/run_tests.py
```
