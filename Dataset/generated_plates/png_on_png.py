import os
from PIL import Image

filename = 'test2.png'
ironman = Image.open(filename, 'r')
filename1 = 'test1.png'
bg = Image.open(filename1, 'r')
text_img = Image.new('RGBA', (600,320), (0, 0, 0, 0))
text_img.paste(bg, (0,0))
text_img.paste(ironman, (0,0), mask=ironman)
text_img.save("out.png", format="png")