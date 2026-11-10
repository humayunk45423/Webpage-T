import asyncio
import os
from playwright.async_api import async_playwright
from PIL import Image

async def analyze_motto_clipping():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 390, 'height': 844})
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        await page.goto(url)
        
        css = """
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
            line-height: 1.26 !important;
            padding: 4px 2px 6px !important;
            white-space: nowrap !important;
            -webkit-box-decoration-break: clone;
            box-decoration-break: clone;
        }
        """
        await page.add_style_tag(content=css)
        
        for lang in ['bn', 'en']:
            await page.evaluate(f'applyLanguage("{lang}")')
            await page.wait_for_timeout(100)
            
            motto_el = page.locator('.hero-motto')
            shot_path = f"tests/motto_crop_{lang}.png"
            await motto_el.screenshot(path=shot_path)
            
            img = Image.open(shot_path).convert('RGB')
            w, h = img.size
            
            # Motto is red gradient, text pixels have red component > 150 or not pure card background
            # Card background is (250..255, 250..255, 250..255)
            top_blank = 0
            for y in range(h):
                row_has_text = any(img.getpixel((x, y))[0] > 180 and img.getpixel((x, y))[1] < 100 for x in range(w))
                if not row_has_text:
                    top_blank += 1
                else:
                    break
                    
            bot_blank = 0
            for y in range(h - 1, -1, -1):
                row_has_text = any(img.getpixel((x, y))[0] > 180 and img.getpixel((x, y))[1] < 100 for x in range(w))
                if not row_has_text:
                    bot_blank += 1
                else:
                    break
            print(f"Motto text ({lang.upper()}): image {w}x{h}, top margin = {top_blank}px, bottom margin = {bot_blank}px")
            assert top_blank >= 2, f"Top clipped in {lang}!"
            assert bot_blank >= 2, f"Bottom clipped in {lang}!"
            
        print("ALL MOTTO CLIPPING CHECKS PASSED WITH GENEROUS MARGINS!")
        await browser.close()

asyncio.run(analyze_motto_clipping())

