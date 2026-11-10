import asyncio
import os
from playwright.async_api import async_playwright

async def compare_fonts():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        await page.goto(url)
        await page.evaluate('applyLanguage("bn")')
        await page.wait_for_timeout(200)
        
        # 1. Noto Sans Bengali with letter-spacing: 0
        css_noto = """
        .lang-bn .hero-title,
        .lang-bn .hero-brand-name,
        .lang-bn .hero-motto {
            letter-spacing: 0 !important;
            font-family: 'Noto Sans Bengali', sans-serif !important;
        }
        """
        await page.add_style_tag(content=css_noto)
        await page.locator('#hero').screenshot(path="tests/desk_bn_noto_zero_spacing.png")
        
        # 2. Anek Bangla with weight 800
        css_anek = """
        .lang-bn .hero-title,
        .lang-bn .hero-brand-name,
        .lang-bn .hero-motto {
            letter-spacing: 0 !important;
            font-family: 'Anek Bangla', sans-serif !important;
            font-weight: 800 !important;
        }
        """
        await page.add_style_tag(content=css_anek)
        await page.locator('#hero').screenshot(path="tests/desk_bn_anek.png")
        
        await browser.close()
        print("Captured comparisons!")

asyncio.run(compare_fonts())

