from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 360, "height": 740})
    page.goto(url)
    
    measure_script = """
    function measure(selector) {
        const el = document.querySelector(selector);
        const style = window.getComputedStyle(el);
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        ctx.font = `${style.fontWeight} ${style.fontSize} ${style.fontFamily}`;
        return {
            text: el.innerText.trim(),
            width: ctx.measureText(el.innerText.trim()).width,
            fontSize: style.fontSize
        };
    }
    window.measure = measure;
    """
    page.add_script_tag(content=measure_script)
    
    for t_size in ["clamp(1.5rem, 6.2vw, 2.05rem)", "clamp(1.65rem, 6.8vw, 2.2rem)", "clamp(1.75rem, 7.2vw, 2.35rem)"]:
        page.add_style_tag(content=f"@media (max-width: 768px) {{ .hero-title {{ font-size: {t_size} !important; }} }}")
        print(f"\n=== Title font size: {t_size} ===")
        for lang in ['bn', 'en']:
            page.evaluate(f"applyLanguage('{lang}')")
            res_brand = page.evaluate("measure('.hero-brand-name')")
            res_motto = page.evaluate("measure('.hero-motto')")
            res_badge = page.evaluate("measure('.hero-badge.apple-specialist-badge span')")
            print(f"[{lang.upper()}] Brand text: '{res_brand['text']}' -> {res_brand['width']:.1f}px (font: {res_brand['fontSize']})")
            print(f"[{lang.upper()}] Motto text: '{res_motto['text']}' -> {res_motto['width']:.1f}px (font: {res_motto['fontSize']})")
            print(f"[{lang.upper()}] Badge text: '{res_badge['text']}' -> {res_badge['width']:.1f}px (font: {res_badge['fontSize']})")
            
    page.close()
    browser.close()

