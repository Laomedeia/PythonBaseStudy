#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'neptune'

from PIL import Image, ImageDraw, ImageFont

#给图片加上一个红色的角标
def addBadges():
    pic = Image.open("/Users/neptune/Pictures/pic/Europa-Galileo-600x444.jpg")
    xsize, ysize = pic.size
    print("xsize: %.2f" % xsize)
    print("ysize: %.2f" % ysize)
    draw = ImageDraw.Draw(pic)
    font = ImageFont.truetype("arial.ttf", xsize / 10)
    draw.text((xsize * 0.90, 0), "V", (250, 128, 114), font)
    pic.save("/Users/neptune/Pictures/pic/Europa-Fix.jpg")

addBadges()
