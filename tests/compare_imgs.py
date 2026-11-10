from PIL import Image

img_clipped = Image.open("tests/title_en_clipped.png")
img_fixed = Image.open("tests/title_en_fixed.png")

print("Clipped size:", img_clipped.size)
print("Fixed size:", img_fixed.size)

