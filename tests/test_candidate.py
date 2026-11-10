from playwright.sync_api import sync_playwright
from PIL import Image
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

candidate_css = """
.hero-title {
    font-size: clamp(2.05rem, 2.85vw, 2.85rem) !important;
    font-weight: 900 !important;
    letter-spacing: -0.025em !important;
    line-height: 1.25 !important;
    margin-bottom: 16px !important;
    text-align: left !important;
    padding: 6px 0 !important;
}

.hero-brand-name {
    display: block !important;
    line-height: 1.22 !important;
    margin-bottom: 6px !important;
    padding: 2px 0 !important;
    white-space: nowrap !important;
}

.hero-motto {
    display: block !important;
    line-height: 1.28 !important;
    margin-top: 0 !important;
    padding: 4px 2px 6px !important;
    white-space: nowrap !important;
}

.red-gradient-text {
    background: linear-gradient(135deg, var(--text-primary) 10%, #f1aeb5 50%, var(--red-main) 100%);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    box-decoration-break: clone !important;
    -webkit-box-decoration-break: clone !important;
}

[data-theme="light"] .red-gradient-text {
    background: linear-gradient(135deg, #0f172a 10%, #b91c1c 60%, var(--red-main) 100%);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}

@media (max-width: 768px) {
    .hero-title {
        font-size: clamp(1.35rem, 5.4vw, 1.85rem) !important;
        line-height: 1.25 !important;
        margin-bottom: 12px !important;
        text-align: center !important;
        padding: 4px 0 !important;
    }
    .hero-brand-name {
        line-height: 1.22 !important;
        margin-bottom: 4px !important;
    }
    .hero-motto {
        line-height: 1.28 !important;
        padding: 2px 2px 4px !important;
    }
}
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(url)
    page.add_style_tag(content=candidate_css)
    
    # Light EN
    page.evaluate("applyTheme('light')")
    page.evaluate("applyLanguage('en')")
    page.wait_for_timeout(200)
    page.locator(".hero-title").screenshot(path="tests/cand_title_en.png")
    
    # Light BN
    page.evaluate("applyLanguage('bn')")
    page.wait_for_timeout(200)
    page.locator(".hero-title").screenshot(path="tests/cand_title_bn.png")
    
    # Mobile
    page.set_viewport_size({"width": 360, "height": 740})
    page.wait_for_timeout(200)
    page.locator(".hero-title").screenshot(path="tests/cand_title_mobile_bn.png")
    page.evaluate("applyLanguage('en')")
    page.wait_for_timeout(200)
    page.locator(".hero-title").screenshot(path="tests/cand_title_mobile_en.png")
    
    page.close()
    browser.close()

def check_bounds(path):
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    min_y = h
    max_y = 0
    # check full image text bounds
    for y in range(h):
        for x in range(w):
            r, g, b, a = img.getpixel((x, y))
            if r < 230 or g < 230 or b < 230:
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    top_pad = min_y
    bot_pad = h - 1 - max_y
    print(f"[{path}] h={h}px, text: y={min_y}..{max_y} | top padding={top_pad}px | bottom padding={bot_pad}px")
    assert top_pad >= 2, f"Top clipped on {path}!"
    assert bot_pad >= 2, f"Bottom clipped on {path}!"
    print("  -> PASS: 100% fully contained with safe margins, zero clipping!")

check_bounds("tests/cand_title_en.png")
check_bounds("tests/cand_title_bn.png")
check_bounds("tests/cand_title_mobile_en.png")
check_bounds("tests/cand_title_mobile_bn.png")

