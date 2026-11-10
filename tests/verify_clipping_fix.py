from playwright.sync_api import sync_playwright
from PIL import Image
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

fix_css = """
.hero-brand-name {
    display: block !important;
    line-height: 1.18 !important;
    margin-bottom: 2px !important;
    white-space: nowrap !important;
}

.hero-motto {
    display: block !important;
    line-height: 1.25 !important;
    margin-top: 0 !important;
    white-space: nowrap !important;
}

.red-gradient-text {
    background: linear-gradient(135deg, var(--text-primary) 10%, #f1aeb5 50%, var(--red-main) 100%);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    display: inline-block !important;
    padding-top: 0.16em !important;
    padding-bottom: 0.22em !important;
    padding-right: 0.05em !important;
    margin-top: -0.16em !important;
    margin-bottom: -0.22em !important;
    margin-right: -0.05em !important;
    box-decoration-break: clone !important;
    -webkit-box-decoration-break: clone !important;
}

[data-theme="light"] .red-gradient-text {
    background: linear-gradient(135deg, #0f172a 10%, #b91c1c 60%, var(--red-main) 100%);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(url)
    page.add_style_tag(content=fix_css)
    
    # Light EN
    page.evaluate("applyTheme('light')")
    page.evaluate("applyLanguage('en')")
    page.wait_for_timeout(200)
    page.locator(".hero-title").screenshot(path="tests/fixed_title_en.png")
    
    # Light BN
    page.evaluate("applyLanguage('bn')")
    page.wait_for_timeout(200)
    page.locator(".hero-title").screenshot(path="tests/fixed_title_bn.png")
    
    # Mobile
    page.set_viewport_size({"width": 360, "height": 740})
    page.wait_for_timeout(200)
    page.locator(".hero-title").screenshot(path="tests/fixed_title_mobile_bn.png")
    page.evaluate("applyLanguage('en')")
    page.wait_for_timeout(200)
    page.locator(".hero-title").screenshot(path="tests/fixed_title_mobile_en.png")
    
    page.close()
    browser.close()

# Now inspect if y and Bengali glyphs are cut off
print("Screenshots taken, verifying...")

