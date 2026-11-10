import asyncio
import os
from playwright.async_api import async_playwright
from PIL import Image

async def analyze_clipping():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 390, 'height': 844})
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        await page.goto(url)
        
        css = """
        .hero-title {
            padding: 2px 0 !important;
            margin-bottom: 12px !important;
        }
        .hero-brand-name {
            font-size: clamp(2.15rem, 10.0vw, 2.50rem) !important;
            letter-spacing: -0.025em;
            line-height: 1.22 !important;
            margin-bottom: 2px !important;
            padding: 6px 2px 5px !important;
            white-space: nowrap !important;
        }
        .hero-motto {
            font-size: clamp(1.50rem, 6.4vw, 2.05rem) !important;
            letter-spacing: -0.02em;
            line-height: 1.24 !important;
            padding: 2px 2px 4px !important;
            white-space: nowrap !important;
        }
        """
        await page.add_style_tag(content=css)
        
        for lang in ['bn', 'en']:
            await page.evaluate(f'applyLanguage("{lang}")')
            await page.wait_for_timeout(100)
            
            brand_el = page.locator('.hero-brand-name')
            shot_path = f"tests/brand_crop_{lang}.png"
            await brand_el.screenshot(path=shot_path)
            
            # Analyze image with PIL
            img = Image.open(shot_path).convert('RGB')
            w, h = img.size
            
            # Text pixels are dark: R < 120 and G < 120 and B < 120
            top_blank = 0
            for y in range(h):
                row_has_text = any(sum(img.getpixel((x, y))) / 3 < 120 for x in range(w))
                if not row_has_text:
                    top_blank += 1
                else:
                    break
                    
            bot_blank = 0
            for y in range(h - 1, -1, -1):
                row_has_text = any(sum(img.getpixel((x, y))) / 3 < 120 for x in range(w))
                if not row_has_text:
                    bot_blank += 1
                else:
                    break
            print(f"Brand text ({lang.upper()}): image {w}x{h}, top margin = {top_blank}px, bottom margin = {bot_blank}px")
            assert top_blank >= 2, f"Top clipped in {lang}!"
            assert bot_blank >= 2, f"Bottom clipped in {lang}!"
            
        print("ALL BRAND CLIPPING CHECKS PASSED WITH GENEROUS MARGINS!")
        await browser.close()

asyncio.run(analyze_clipping())
