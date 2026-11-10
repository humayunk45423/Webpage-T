from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 360, "height": 740})
    page.goto(url)
    
    for lang in ['bn', 'en']:
        page.evaluate(f"applyLanguage('{lang}')")
        page.wait_for_timeout(100)
        badge = page.locator(".hero-badge.apple-specialist-badge")
        badge.screenshot(path=f"tests/badge_check_{lang}.png")
        
    page.close()
    browser.close()

from PIL import Image

def check_badge(path):
    img = Image.open(path).convert("RGB")
    w, h = img.size
    min_y, max_y = h, 0
    for y in range(h):
        for x in range(w):
            r, g, b = img.getpixel((x, y))
            # check non-background
            if r < 200 or g < 200 or b < 200:
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    print(f"[{path}] h={h}px, text: y={min_y}..{max_y} | top pad={min_y}px | bot pad={h - 1 - max_y}px")

check_badge("tests/badge_check_bn.png")
check_badge("tests/badge_check_en.png")

