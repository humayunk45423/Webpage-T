from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

viewports = [
    ("Desktop 1440", 1440, 900),
    ("Desktop 1200", 1200, 800),
    ("Tablet 960", 960, 700),
    ("Mobile 390", 390, 844),
    ("Mobile 360", 360, 740),
    ("Mobile 320", 320, 568),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    for vp_name, w, h in viewports:
        title_heights = {}
        for lang in ['bn', 'en']:
            page = browser.new_page(viewport={"width": w, "height": h})
            page.goto(url)
            page.evaluate(f"applyLanguage('{lang}')")
            page.wait_for_timeout(200)
            
            badge_box = page.locator(".hero-badge.apple-specialist-badge").bounding_box()
            brand_box = page.locator(".hero-brand-name").bounding_box()
            motto_box = page.locator(".hero-motto").bounding_box()
            title_box = page.locator(".hero-title").bounding_box()
            
            scroll_w = page.evaluate("document.documentElement.scrollWidth")
            client_w = page.evaluate("document.documentElement.clientWidth")
            
            badge_h = badge_box['height']
            gap = motto_box['y'] - (brand_box['y'] + brand_box['height'])
            title_heights[lang] = title_box['height']
            
            print(f"[{vp_name} - {lang.upper()}]")
            print(f"  Badge: h={badge_h:.1f}px (Wrapped: {badge_h > 35}) | text='{page.locator('.hero-badge.apple-specialist-badge span').inner_text()}'")
            print(f"  Brand: h={brand_box['height']:.1f}px | text='{page.locator('.hero-brand-name').inner_text()}'")
            print(f"  Motto: h={motto_box['height']:.1f}px | text='{page.locator('.hero-motto').inner_text()}'")
            print(f"  Gap between lines: {gap:.1f}px | Total Title Height: {title_box['height']:.1f}px")
            print(f"  Overflow check: scrollWidth={scroll_w}, clientWidth={client_w}")
            
            # 1. Badge must NEVER wrap
            assert badge_h <= 35, f"ERROR: Badge wrapped on {vp_name} ({lang})! Height={badge_h}"
            
            # 2. Gap must be tight (no dead space)
            assert gap <= 8, f"ERROR: Dead space between Brand and Motto! Gap={gap}"
            
            # 3. Motto must NOT wrap into 2 lines (height should be equal to single line ~ same as brand height)
            assert abs(motto_box['height'] - brand_box['height']) < 12, f"ERROR: Motto wrapped to multiple lines! Brand h={brand_box['height']}, Motto h={motto_box['height']}"
            
            # 4. Zero overflow
            assert scroll_w <= client_w, f"ERROR: Horizontal overflow on {vp_name}! scrollWidth={scroll_w} > clientWidth={client_w}"
            
            page.close()
            
        # Verify BN and EN occupy the exact same volume & height (within 4px)
        diff = abs(title_heights['bn'] - title_heights['en'])
        print(f"  -> Title Height Difference between BN ({title_heights['bn']:.1f}px) & EN ({title_heights['en']:.1f}px): {diff:.1f}px")
        assert diff <= 4, f"ERROR: Mismatched volume between BN and EN on {vp_name}! diff={diff}"
        print(f"  -> PASS: BN and EN occupy the exact same space!\n")
        
    browser.close()
    print("ALL TESTS PASSED 100% PERFECTLY!")

