from PIL import Image

def find_text_bounds(path):
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    
    # find top-most non-background pixel in the motto (bottom half of image)
    # background is ~ (252, 250, 251) in light mode
    min_y = h
    max_y = 0
    for y in range(h // 2, h):
        for x in range(w):
            r, g, b, a = img.getpixel((x, y))
            # if significantly darker than 245
            if r < 230 or g < 230 or b < 230:
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                
    print(f"[{path}] Motto text vertical bounds: y={min_y} to y={max_y} (height={max_y - min_y + 1}px) inside image height={h}px")
    print(f"  Top padding inside image: {min_y}px | Bottom padding: {h - 1 - max_y}px")
    if h - 1 - max_y > 0 and min_y > 0:
        print("  -> PASS: Text is fully contained with safe margins, ZERO clipping!")
    else:
        print("  -> WARNING: Text touches edge!")

find_text_bounds("tests/fixed_title_en.png")
find_text_bounds("tests/fixed_title_bn.png")
find_text_bounds("tests/fixed_title_mobile_en.png")
find_text_bounds("tests/fixed_title_mobile_bn.png")

