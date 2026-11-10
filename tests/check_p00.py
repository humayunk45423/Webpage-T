from PIL import Image

img = Image.open("tests/cand_title_en.png")
print("Pixel at 0,0:", img.getpixel((0,0)))

