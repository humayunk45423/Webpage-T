from playwright.sync_api import sync_playwright
from PIL import Image
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

def is_text_pixel(p):
    r, g, b = p[:3]
    # dark text
    if r < 140 and g < 140 and b < 140:
        return True
    # red gradient text
    if r > 160 and g < 90 and b < 100:
        return True
    return False

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(url)
    
    # 1. Light EN
    page.evaluate("applyTheme('light')")
    page.evaluate("applyLanguage('en')")
    page.wait_for_timeout(250)
    page.locator(".hero-title").screenshot(path="tests/live_title_en.png")
    
    # 2. Light BN
    page.evaluate("applyLanguage('bn')")
    page.wait_for_timeout(250)
    page.locator(".hero-title").screenshot(path="tests/live_title_bn.png")
    
    # 3. Mobile BN & EN
    page.set_viewport_size({"width": 360, "height": 740})
    page.wait_for_timeout(250)
    page.locator(".hero-title").screenshot(path="tests/live_title_mobile_bn.png")
    page.locator(".hero-badge.apple-specialist-badge").screenshot(path="tests/live_badge_mobile_bn.png")
    
    page.evaluate("applyLanguage('en')")
    page.wait_for_timeout(250)
    page.locator(".hero-title").screenshot(path="tests/live_title_mobile_en.png")
    page.locator(".hero-badge.apple-specialist-badge").screenshot(path="tests/live_badge_mobile_en.png")
    
    page.close()
    browser.close()

def check_real_text_bounds(path):
    img = Image.open(path).convert("RGB")
    w, h = img.size
    min_y, max_y = h, 0
    for y in range(h):
        for x in range(w):
            if is_text_pixel(img.getpixel((x, y))):
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    top_pad = min_y
    bot_pad = h - 1 - max_y
    print(f"[{path}] h={h}px, text: y={min_y}..{max_y} | top padding={top_pad}px | bottom padding={bot_pad}px")
    assert top_pad >= 2, f"FAILED: Top clipped on {path}! top_pad={top_pad}"
    assert bot_pad >= 2, f"FAILED: Bottom clipped on {path}! bot_pad={bot_pad}"
    print(f"  -> PASS: 100% UNCLIPPED with generous padding!\n")

check_real_text_bounds("tests/live_title_en.png")
check_real_text_bounds("tests/live_title_bn.png")
check_real_text_bounds("tests/live_title_mobile_en.png")
check_real_text_bounds("tests/live_title_mobile_bn.png")
print("ALL LIVE RENDER BOUNDS CHECK PASSED!")

