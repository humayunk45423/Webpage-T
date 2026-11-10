from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    # Check Desktop 1440x900 in BN and EN
    for lang in ['bn', 'en']:
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(url)
        page.evaluate(f"applyLanguage('{lang}')")
        page.wait_for_timeout(300)
        
        brand_box = page.locator(".hero-brand-name").bounding_box()
        motto_box = page.locator(".hero-motto").bounding_box()
        title_box = page.locator(".hero-title").bounding_box()
        badge_box = page.locator(".hero-badge.apple-specialist-badge").bounding_box()
        
        print(f"=== DESKTOP 1440 ({lang.upper()}) ===")
        print("  Badge box:", badge_box)
        print("  Brand box:", brand_box)
        print("  Motto box:", motto_box)
        print("  Title total box:", title_box)
        gap_between = motto_box["y"] - (brand_box["y"] + brand_box["height"])
        print("  Gap between Brand & Motto:", gap_between)
        print("  Motto height (is it multi-line?):", motto_box["height"])
        page.close()

    # Check Mobile 360x740 in BN and EN
    for lang in ['bn', 'en']:
        page = browser.new_page(viewport={"width": 360, "height": 740})
        page.goto(url)
        page.evaluate(f"applyLanguage('{lang}')")
        page.wait_for_timeout(300)
        
        brand_box = page.locator(".hero-brand-name").bounding_box()
        motto_box = page.locator(".hero-motto").bounding_box()
        title_box = page.locator(".hero-title").bounding_box()
        badge_box = page.locator(".hero-badge.apple-specialist-badge").bounding_box()
        badge_text_height = page.locator(".hero-badge.apple-specialist-badge span").bounding_box()
        
        print(f"=== MOBILE 360 ({lang.upper()}) ===")
        print("  Badge box:", badge_box)
        print("  Badge span height:", badge_text_height)
        print("  Brand box:", brand_box)
        print("  Motto box:", motto_box)
        print("  Title total box:", title_box)
        gap_between = motto_box["y"] - (brand_box["y"] + brand_box["height"])
        print("  Gap between Brand & Motto:", gap_between)
        print("  Motto height:", motto_box["height"])
        page.close()
        
    browser.close()

