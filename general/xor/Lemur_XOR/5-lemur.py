#!/usr/bin/python3

# NOTE: launch this from terminal or provide full path

from PIL import Image, ImageChops
im1 = Image.open('lemur.png')
im2 = Image.open('flag.png')

# im3 = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))
im3 = ImageChops.subtract(im1, im2)

im3.show()
#im3.save("result.png")