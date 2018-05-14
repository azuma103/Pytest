# -*- coding: utf-8 -*-
import numpy
import photos
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def draw_text_at_center(img, text):
 draw = ImageDraw.Draw(img)
 draw.font = ImageFont.load_default()
 img_size = numpy.array(img.size)
 txt_size = numpy.array(draw.font.getsize(text))
 pos = [1473, 2010] #(img_size - txt_size) / 2
 draw.text(pos, text, (255, 255, 255))

#img1 = photos.pick_image()
img1 = photos.capture_image()
img1.convert('RGBA')
text = "2018/05/14"

draw_text_at_center(img1, text)

img1.show()
saveimg = photos.save_image(img1)

if saveimg is True:
  print ("saved")
