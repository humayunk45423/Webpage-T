from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

css_candidate = """
/* Test Candidate CSS */
.hero-badges-cluster {
    margin-bottom: 12px !important;
}
.hero-badge.apple-specialist-badge {
    white-space: nowrap !important;
    font-size: clamp(0.60rem, 1vw, 0.72rem) !important;
    padding: 5px 12px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    max-width: 100% !important;
}
.hero-title {
    font-size: clamp(1.9rem, 2.85vw, 2.9rem) !important;
    font-weight: 900 !important;
    letter-spacing: -0.025em !important;
    margin-bottom: 16px !important;
    text-align: left !important;
    line-height: 1.1 !important;
}
.hero-brand-name {
    display: block !important;
    line-height: 1.08 !important;
    margin-bottom: 4px !important;
    white-space: nowrap !important;
}
.hero-motto {
    display: block !important;
    line-height: 1.12 !important;
    margin-top: 0 !important;
    white-space: nowrap !important;
}

@media (max-width: 768px) {
    .hero-badges-cluster {
        margin-bottom: 8px !important;
    }
    .hero-badge.apple-specialist-badge {
        font-size: clamp(0.56rem, 2.6vw, 0.68rem) !important;
        padding: 4px 10px !important;
    }
    .hero-title {
        font-size: clamp(1.35rem, 5.4vw, 1.85rem) !important;
        margin-bottom: 10px !important;
        text-align: center !important;
    }
    .hero-brand-name {
        margin-bottom: 3px !important;
    }
}
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    test_viewports = [
        ("Desktop 1440", 1440, 900),
        ("Desktop 1200", 1200, 800),
        ("Tablet 960", 960, 700),
        ("Mobile 390", 390, 844),
        ("Mobile 360", 360, 740),
        ("Mobile 320", 320, 568),
    ]
    
    for vp_name, w, h in test_viewports:
        for lang in ['bn', 'en']:
            page = browser.new_page(viewport={"width": w, "height": h})
            page.goto(url)
            page.evaluate(f"applyLanguage('{lang}')")
            # remove <br> inside .hero-title
            page.evaluate("document.querySelectorAll('.hero-title br').forEach(b => b.remove())")
            page.add_style_tag(content=css_candidate)
            page.wait_for_timeout(100)
            
            badge_box = page.locator(".hero-badge.apple-specialist-badge").bounding_box()
            brand_box = page.locator(".hero-brand-name").bounding_box()
            motto_box = page.locator(".hero-motto").bounding_box()
            title_box = page.locator(".hero-title").bounding_box()
            
            badge_h = badge_box['height']
            gap = motto_box['y'] - (brand_box['y'] + brand_box['height'])
            
            print(f"[{vp_name}] ({lang.upper()}):")
            print(f"  Badge: w={badge_box['width']:.1f}, h={badge_h:.1f} (Wrapped: {badge_h > 34})")
            print(f"  Brand: w={brand_box['width']:.1f}, h={brand_box['height']:.1f}")
            print(f"  Motto: w={motto_box['width']:.1f}, h={motto_box['height']:.1f}")
            print(f"  Gap between lines: {gap:.1f}px | Total Title Height: {title_box['height']:.1f}px")
            
            # Assertions
            if w <= 360:
                assert badge_h <= 34, f"Badge wrapped on {vp_name} {lang}! height={badge_h}"
            assert gap < 12, f"Dead space between Brand and Motto too big! gap={gap}"
            page.close()
            
    browser.close()
    print("\nALL SIZING TESTS PASSED FLAWLESSLY!")
