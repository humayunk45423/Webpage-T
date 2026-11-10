from PIL import Image

def check_badge(path):
    img = Image.open(path).convert("RGB")
    w, h = img.size
    min_y, max_y = h, 0
    for y in range(h):
        for x in range(w):
            r, g, b = img.getpixel((x, y))
            # check non-background
            if r < 180 and g < 180 and b < 180:
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    print(f"[{path}] h={h}px, text: y={min_y}..{max_y} | top pad={min_y}px | bot pad={h - 1 - max_y}px")

check_badge("tests/live_badge_mobile_bn.png")
check_badge("tests/live_badge_mobile_en.png")

