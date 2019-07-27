#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/26 16:22
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : pillow1.py
# @Software   : PyCharm
# @Description: 使用pillow操作图像


from PIL import Image

img = Image.open('./res/test_1.jpg')
print(img.size)
print(img.format)
print(img.format_description)
img.save('./res/handle_1.png')


img2 = Image.open('./res/test_2.jpg')
img_temp = Image.open('./res/test_3.jpg')
img3 = img_temp.crop((0, 0, 500, 500))
for x in range(1):
    for y in range(2):
        img2.paste(img3, (95 * y, 180 *x))
img2.resize((img.size[0] // 2, img.size[1] // 2))
img2.rotate(90)
img2.save('./res/handle_2.png')
