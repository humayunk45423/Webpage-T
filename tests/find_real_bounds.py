from PIL import Image

def is_text_pixel(p):
    r, g, b = p[:3]
    # dark text
    if r < 140 and g < 140 and b < 140:
        return True
    # red gradient text
    if r > 160 and g < 90 and b < 100:
        return True
    return False

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

check_real_text_bounds("tests/cand_title_en.png")
check_real_text_bounds("tests/cand_title_bn.png")
check_real_text_bounds("tests/cand_title_mobile_en.png")
check_real_text_bounds("tests/cand_title_mobile_bn.png")

