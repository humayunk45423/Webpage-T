from PIL import Image

def analyze_bottom(path):
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    # scan from bottom up to find the lowest non-transparent / red pixel
    lowest_y = 0
    for y in range(h - 1, -1, -1):
        for x in range(w):
            r, g, b, a = img.getpixel((x, y))
            # check if it's red or dark text (not white background ~255,255,255)
            if a > 100 and (r < 240 or g < 240 or b < 240):
                lowest_y = y
                break
        if lowest_y > 0:
            break
    print(f"{path}: height={h}, lowest text pixel={lowest_y}, padding below text={h - lowest_y}px")

analyze_bottom("tests/title_en_clipped.png")
analyze_bottom("tests/title_en_fixed.png")
analyze_bottom("tests/title_bn_clipped.png")
analyze_bottom("tests/title_bn_fixed.png")

