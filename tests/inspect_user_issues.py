import asyncio
import os
from playwright.async_api import async_playwright

async def inspect_motto_and_desktop():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        
        # 1. MOBILE MOTTO MEASUREMENTS IN BN
        print("=== MOBILE BN MOTTO SIZING INVESTIGATION ===")
        page = await browser.new_page(viewport={'width': 390, 'height': 844})
        await page.goto(url)
        await page.evaluate('applyLanguage("bn")')
        brand_w = await page.evaluate("""() => {
            const el = document.querySelector('.hero-brand-name');
            const range = document.createRange();
            range.selectNodeContents(el);
            return range.getBoundingClientRect().width;
        }""")
        print(f"Target Brand Width in BN (390px): {brand_w:.1f}px")
        
        # Try different font-size and word-spacing / letter-spacing for .lang-bn .hero-motto
        for fsize in [1.8, 1.85, 1.9, 1.95, 2.0, 2.05, 2.1, 2.15]:
            await page.evaluate(f"""() => {{
                document.querySelector('.hero-motto').style.fontSize = '{fsize}rem';
            }}""")
            motto_w = await page.evaluate("""() => {
                const el = document.querySelector('.hero-motto');
                const range = document.createRange();
                range.selectNodeContents(el);
                return range.getBoundingClientRect().width;
            }""")
            print(f"Motto fsize={fsize}rem -> width={motto_w:.1f}px (diff vs brand: {motto_w - brand_w:+.1f}px)")
            
        await page.close()
        
        # 2. DESKTOP SPACING INVESTIGATION
        print("\n=== DESKTOP SPACING COMPARISON ===")
        dpage = await browser.new_page(viewport={'width': 1440, 'height': 900})
        await dpage.goto(url)
        
        for lang in ['en', 'bn']:
            await dpage.evaluate(f'applyLanguage("{lang}")')
            await dpage.wait_for_timeout(100)
            
            # Measure desktop title brand vs motto width
            desk_brand_w = await dpage.evaluate("""() => {
                const el = document.querySelector('.hero-brand-name');
                const range = document.createRange();
                range.selectNodeContents(el);
                return range.getBoundingClientRect().width;
            }""")
            desk_motto_w = await dpage.evaluate("""() => {
                const el = document.querySelector('.hero-motto');
                const range = document.createRange();
                range.selectNodeContents(el);
                return range.getBoundingClientRect().width;
            }""")
            desc_lines = await dpage.evaluate("""() => {
                const el = document.querySelector('.hero-desc');
                return {
                    height: el.offsetHeight,
                    lineHeight: getComputedStyle(el).lineHeight,
                    text: el.innerText
                };
            }""")
            print(f"Desktop {lang.upper()}:")
            print(f"  Brand Width = {desk_brand_w:.1f}px, Motto Width = {desk_motto_w:.1f}px (diff: {desk_motto_w - desk_brand_w:+.1f}px)")
            print(f"  Desc height = {desc_lines['height']}px (lineHeight={desc_lines['lineHeight']})")
            
        await dpage.close()
        await browser.close()

asyncio.run(inspect_motto_and_desktop())

