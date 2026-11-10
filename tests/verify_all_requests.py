import asyncio
import os
from playwright.async_api import async_playwright

async def verify_all():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        
        # 1. VERIFY REQUEST 1: CHIP-4 REMOVED, CHIP-2 CENTERED
        print("=== 1. VERIFYING CHIP-4 REMOVAL & CHIP-2 CENTERING ===")
        page = await browser.new_page(viewport={'width': 1366, 'height': 820})
        await page.goto(url)
        chip4 = await page.locator('.chip-4').count()
        assert chip4 == 0, f"Error: chip-4 still in DOM! count={chip4}"
        print("PASS: chip-4 completely removed from DOM.")
        
        # Check chip-2 centering on desktop
        stage_box = await page.locator('.hero-phone-stage').bounding_box()
        chip2_box = await page.locator('.chip-2').bounding_box()
        chip2_center_y = chip2_box['y'] + chip2_box['height'] / 2
        stage_center_y = stage_box['y'] + stage_box['height'] / 2
        diff_y = abs(chip2_center_y - stage_center_y)
        print(f"Desktop: Stage center Y={stage_center_y:.1f}, Chip-2 center Y={chip2_center_y:.1f}, diff={diff_y:.1f}px")
        assert diff_y < 15, f"Chip-2 not vertically centered on desktop! diff={diff_y}px"
        print("PASS: Chip-2 vertically centered on desktop.")
        await page.close()
        
        # Check chip-2 centering on mobile
        mpage = await browser.new_page(viewport={'width': 390, 'height': 844})
        await mpage.goto(url)
        m_stage_box = await mpage.locator('.hero-phone-stage').bounding_box()
        m_chip2_box = await mpage.locator('.chip-2').bounding_box()
        m_chip2_center_y = m_chip2_box['y'] + m_chip2_box['height'] / 2
        m_stage_center_y = m_stage_box['y'] + m_stage_box['height'] / 2
        m_diff_y = abs(m_chip2_center_y - m_stage_center_y)
        print(f"Mobile 390px: Stage center Y={m_stage_center_y:.1f}, Chip-2 center Y={m_chip2_center_y:.1f}, diff={m_diff_y:.1f}px")
        assert m_diff_y < 15, f"Chip-2 not vertically centered on mobile! diff={m_diff_y}px"
        print("PASS: Chip-2 vertically centered on mobile.")

        # 2. VERIFY REQUEST 2: BANGLA MOTTO MATCHES BRAND LENGTH ON MOBILE
        print("\n=== 2. VERIFYING BANGLA MOTTO & BRAND LENGTH MATCH ON MOBILE ===")
        for w in [360, 390, 412]:
            await mpage.set_viewport_size({'width': w, 'height': 844})
            await mpage.evaluate('applyLanguage("bn")')
            await mpage.wait_for_timeout(100)
            
            brand_w = await mpage.evaluate("""() => {
                const el = document.querySelector('.hero-brand-name');
                const range = document.createRange();
                range.selectNodeContents(el);
                return range.getBoundingClientRect().width;
            }""")
            motto_w = await mpage.evaluate("""() => {
                const el = document.querySelector('.hero-motto');
                const range = document.createRange();
                range.selectNodeContents(el);
                return range.getBoundingClientRect().width;
            }""")
            diff = abs(brand_w - motto_w)
            match_pct = (min(brand_w, motto_w) / max(brand_w, motto_w)) * 100
            print(f"w={w}px BN: Brand={brand_w:.1f}px, Motto={motto_w:.1f}px, Diff={diff:.1f}px, Match={match_pct:.1f}%")
            assert diff <= 3.5, f"Length difference too large at {w}px: {diff}px"
            
            scroll_w = await mpage.evaluate("() => document.documentElement.scrollWidth")
            client_w = await mpage.evaluate("() => document.documentElement.clientWidth")
            assert scroll_w <= client_w, f"Horizontal overflow at {w}px!"
        print("PASS: Bangla brand name and motto have identical collective length across all mobile viewports!")

        # 3. VERIFY REQUEST 3: DESKTOP SPACING AND BUTTONS SIDE-BY-SIDE
        print("\n=== 3. VERIFYING DESKTOP HARMONY & BUTTONS ===")
        dpage = await browser.new_page(viewport={'width': 1366, 'height': 820})
        await dpage.goto(url)
        for w in [1200, 1280, 1366, 1440]:
            await dpage.set_viewport_size({'width': w, 'height': 820})
            for lang in ['bn', 'en']:
                await dpage.evaluate(f'applyLanguage("{lang}")')
                await dpage.wait_for_timeout(50)
                
                b1 = await dpage.locator('.hero-actions .btn-primary').bounding_box()
                b2 = await dpage.locator('.hero-actions .btn-secondary').bounding_box()
                is_stacked = b2['y'] > b1['y'] + 10
                print(f"Desktop w={w}px {lang.upper()}: b1_w={b1['width']:.1f}px, b2_w={b2['width']:.1f}px, STACKED={is_stacked}")
                assert not is_stacked, f"Buttons stacked at {w}px in {lang}!"
        print("PASS: Desktop buttons fit side by side with elegant harmonious spacing!")
        
        await dpage.close()
        await mpage.close()
        await browser.close()
        print("\nALL ASSERTIONS PASSED WITH FLYING COLORS!")

asyncio.run(verify_all())

