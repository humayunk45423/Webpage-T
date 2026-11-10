from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

candidate_css = """
.hero-brand-name {
    display: block !important;
    line-height: 1.2 !important;
    padding-top: 0.1em !important;
    padding-bottom: 0.05em !important;
    margin-bottom: 0 !important;
    white-space: nowrap !important;
}

.hero-motto {
    display: block !important;
    line-height: 1.25 !important;
    padding-top: 0.15em !important;
    padding-bottom: 0.22em !important;
    margin-top: -0.05em !important;
    margin-bottom: -0.15em !important;
    white-space: nowrap !important;
}

.red-gradient-text {
    /* Ensure background extends comfortably beyond font glyph bounds */
    display: inline-block !important;
    box-decoration-break: clone !important;
    -webkit-box-decoration-break: clone !important;
}
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(url)
    page.add_style_tag(content=candidate_css)
    
    # 1. English Light Mode
    page.evaluate("applyLanguage('en')")
    page.evaluate("applyTheme('light')")
    page.wait_for_timeout(300)
    page.locator(".hero-title").screenshot(path="tests/title_en_fixed.png")
    
    # 2. Bengali Light Mode
    page.evaluate("applyLanguage('bn')")
    page.wait_for_timeout(300)
    page.locator(".hero-title").screenshot(path="tests/title_bn_fixed.png")
    
    # 3. Mobile BN & EN
    page.set_viewport_size({"width": 360, "height": 740})
    page.locator(".hero-title").screenshot(path="tests/title_mobile_bn_fixed.png")
    page.evaluate("applyLanguage('en')")
    page.wait_for_timeout(300)
    page.locator(".hero-title").screenshot(path="tests/title_mobile_en_fixed.png")
    
    page.close()
    browser.close()
print("Candidate screenshots captured")

