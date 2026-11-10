from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    # 1. Test Desktop 1440x900
    page_d = browser.new_page(viewport={"width": 1440, "height": 900})
    page_d.goto(url)
    page_d.wait_for_timeout(300)
    visual_box = page_d.locator(".hero-visual-col").bounding_box()
    content_box = page_d.locator(".hero-content-col").bounding_box()
    print("Desktop 1440x900:")
    print("  Visual x:", visual_box["x"], "w:", visual_box["width"])
    print("  Content x:", content_box["x"], "w:", content_box["width"])
    if visual_box["x"] < content_box["x"]:
        print("  PASS: Visual is on the LEFT, content is on the RIGHT on desktop!")
    else:
        print("  FAIL: Visual is not on the left!")
    page_d.close()
    
    # 2. Test Mobile 360x640 & 390x844
    for w, h in [(360, 640), (390, 844)]:
        page_m = browser.new_page(viewport={"width": w, "height": h})
        page_m.goto(url)
        page_m.evaluate("applyLanguage('bn')")
        page_m.wait_for_timeout(300)
        
        scroll_w = page_m.evaluate("document.documentElement.scrollWidth")
        client_w = page_m.evaluate("document.documentElement.clientWidth")
        print(f"Mobile {w}x{h}: scrollWidth={scroll_w}, clientWidth={client_w}")
        
        # Verify vertical order
        badge_y = page_m.locator(".hero-badges-cluster").bounding_box()["y"]
        title_y = page_m.locator(".hero-title").bounding_box()["y"]
        vis_y = page_m.locator(".hero-visual-col").bounding_box()["y"]
        actions_y = page_m.locator(".hero-actions").bounding_box()["y"]
        desc_y = page_m.locator(".hero-desc").bounding_box()["y"]
        stats_y = page_m.locator(".hero-stats-row").bounding_box()["y"]
        
        print(f"  Mobile Order Y coordinates: Badge={badge_y}, Title={title_y}, Vis={vis_y}, Actions={actions_y}, Desc={desc_y}, Stats={stats_y}")
        
        if badge_y < title_y < vis_y < actions_y < desc_y < stats_y:
            print("  PASS: Mobile elements are in the exact 1-8 order!")
        else:
            print("  FAIL: Mobile ordering mismatch!")
            
        page_m.close()
        
    browser.close()

