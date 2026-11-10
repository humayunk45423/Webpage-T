import asyncio
import os
from playwright.async_api import async_playwright
from PIL import Image

async def verify_final():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        
        print("=== 1. VERIFYING BRAND WIDTH VS BADGE WIDTH & OVERFLOW ===")
        for w in [320, 360, 375, 390, 412, 430]:
            page = await browser.new_page(viewport={'width': w, 'height': 800})
            await page.goto(url)
            
            for lang in ['bn', 'en']:
                await page.evaluate(f'applyLanguage("{lang}")')
                await page.wait_for_timeout(50)
                
                badge_w = await page.evaluate("() => document.querySelector('.apple-specialist-badge').getBoundingClientRect().width")
                brand_w = await page.evaluate("""() => {
                    const el = document.querySelector('.hero-brand-name');
                    const range = document.createRange();
                    range.selectNodeContents(el);
                    return range.getBoundingClientRect().width;
                }""")
                motto_w = await page.evaluate("""() => {
                    const el = document.querySelector('.hero-motto');
                    const range = document.createRange();
                    range.selectNodeContents(el);
                    return range.getBoundingClientRect().width;
                }""")
                scroll_w = await page.evaluate("() => document.documentElement.scrollWidth")
                client_w = await page.evaluate("() => document.documentElement.clientWidth")
                overflow = scroll_w > client_w
                ratio = (brand_w / badge_w) * 100
                print(f"w={w}px | {lang.upper()}: Badge={badge_w:.1f}px, Brand={brand_w:.1f}px ({ratio:.1f}%), Motto={motto_w:.1f}px, Overflow={overflow}")
                assert not overflow, f"Overflow detected at {w}px in {lang}!"
            await page.close()

        print("\n=== 2. VERIFYING GLYPH CLIPPING MARGINS ===")
        page = await browser.new_page(viewport={'width': 390, 'height': 844})
        await page.goto(url)
        for lang in ['bn', 'en']:
            await page.evaluate(f'applyLanguage("{lang}")')
            await page.wait_for_timeout(100)
            
            brand_el = page.locator('.hero-brand-name')
            shot_path = f"tests/final_brand_{lang}.png"
            await brand_el.screenshot(path=shot_path)
            
            img = Image.open(shot_path).convert('RGB')
            w, h = img.size
            top_blank = 0
            for y in range(h):
                if not any(sum(img.getpixel((x, y))) / 3 < 120 for x in range(w)):
                    top_blank += 1
                else:
                    break
            bot_blank = 0
            for y in range(h - 1, -1, -1):
                if not any(sum(img.getpixel((x, y))) / 3 < 120 for x in range(w)):
                    bot_blank += 1
                else:
                    break
            print(f"Brand ({lang.upper()}): top margin = {top_blank}px, bottom margin = {bot_blank}px")
            assert top_blank >= 2, f"Top clipped in {lang}!"
            assert bot_blank >= 2, f"Bottom clipped in {lang}!"
            
        print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")
        await browser.close()

asyncio.run(verify_final())

