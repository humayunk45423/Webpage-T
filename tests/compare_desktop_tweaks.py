import asyncio
import os
from playwright.async_api import async_playwright

async def compare_desktop_tweaks():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        await page.goto(url)
        await page.evaluate('applyLanguage("bn")')
        await page.wait_for_timeout(150)
        
        # Take baseline screenshot
        await page.locator('#hero').screenshot(path="tests/desktop_bn_baseline.png")
        
        # Candidate 1: Letter spacing normal for BN, refined line-height and rhythm
        css_tweak = """
        /* Bengali Typography & Desktop Spacing Perfection */
        .lang-bn .hero-title,
        .lang-bn .hero-brand-name,
        .lang-bn .hero-motto {
            letter-spacing: 0 !important;
        }
        .lang-bn .hero-brand-name {
            font-size: clamp(2.35rem, 3.4vw, 3.4rem) !important;
            line-height: 1.22 !important;
            margin-bottom: 6px !important;
        }
        .lang-bn .hero-motto {
            font-size: clamp(2.2rem, 3.2vw, 3.2rem) !important;
            line-height: 1.28 !important;
            word-spacing: 0.1em;
        }
        .lang-bn .hero-desc {
            font-size: 1.08rem !important;
            line-height: 1.72 !important;
            max-width: 580px !important;
            margin-bottom: 24px !important;
            letter-spacing: 0.01em;
        }
        .lang-bn .hero-actions {
            margin-bottom: 28px !important;
            gap: 14px !important;
        }
        .lang-bn .hero-stats-row {
            padding-top: 16px !important;
        }
        """
        await page.add_style_tag(content=css_tweak)
        await page.wait_for_timeout(150)
        await page.locator('#hero').screenshot(path="tests/desktop_bn_tweak1.png")
        
        # Candidate 2: Using Anek Bangla for display titles in Bengali
        css_tweak2 = """
        .lang-bn .hero-brand-name,
        .lang-bn .hero-motto {
            font-family: 'Anek Bangla', var(--font-bengali) !important;
            font-weight: 800 !important;
            letter-spacing: 0.005em !important;
        }
        """
        await page.add_style_tag(content=css_tweak2)
        await page.wait_for_timeout(150)
        await page.locator('#hero').screenshot(path="tests/desktop_bn_tweak2_anek.png")
        
        await browser.close()
        print("Captured desktop candidates: baseline, tweak1, tweak2_anek")

asyncio.run(compare_desktop_tweaks())

