#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw


# base
w = 1500 
h = 1400
my_image = Image.new(
    mode='RGB', size=(w, h), color='#FFFFFF'
)

out = '#d3d3d3'
draw = ImageDraw.Draw(my_image)

rectangles = [
    (100, 100, 1000, 400),
    (1100, 100, 1400, 900),
    (100, 500, 400, 1300),
    (500, 500, 1000, 900),
    (500, 1000, 1400, 1300)
]

colors = []
print('input 5 color codes (ex. FFFFFF)')

# set color
for i in range(1,6):
    print(str(i) + ':', end='')
    color = input()
    colors.append('#' + color)
print(colors)

dic = {key: val for key, val in zip(colors, rectangles)}
print(dic)

# draw rectangle
for k,v in dic.items():
    draw.rectangle(v, fill=k , outline=out)

# save image
my_image.save('./img.png')
