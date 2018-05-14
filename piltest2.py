# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageDraw

import photos

#img1 = photos.pick_image()
img1 = photos.capture_image()

img1.convert('RGBA')
drawbuffer = ImageDraw.Draw(img1)

img2 = Image.open('kinoco.jpg')
img1.paste(img2, (-102, 648))

img1.show()
saveimg = photos.save_image(img1)

if saveimg is True:
  print ("saved")
