from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch()
    for w in [360, 390, 412]:
        page = browser.new_page(viewport={"width": w, "height": 800})
        page.goto(url)
        page.evaluate("applyLanguage('bn')")
        page.wait_for_timeout(300)
        
        scroll_w = page.evaluate("document.documentElement.scrollWidth")
        client_w = page.evaluate("document.documentElement.clientWidth")
        body_scroll_w = page.evaluate("document.body.scrollWidth")
        
        nav_box = page.locator(".glass-header").bounding_box()
        burger = page.locator("#menu-toggle").bounding_box()
        
        print(f"=== Viewport Width {w} ===")
        print(f"Doc scrollWidth={scroll_w}, clientWidth={client_w}, body scrollWidth={body_scroll_w}")
        print(f"Navbar box: {nav_box}")
        print(f"Hamburger box: {burger}")
        
        bad = page.evaluate("""() => {
            const elms = document.querySelectorAll("*");
            const res = [];
            for (const el of elms) {
                const rect = el.getBoundingClientRect();
                if (rect.right > window.innerWidth + 1 || rect.left < -1) {
                    res.push({ tag: el.tagName, id: el.id, class: String(el.className).slice(0, 30), right: Math.round(rect.right), left: Math.round(rect.left), w: Math.round(rect.width) });
                }
            }
            return res;
        }""")
        print(f"Overflowing elements count: {len(bad)}")
        for b in bad[:10]:
            print("   ", b)
        page.close()
    browser.close()
