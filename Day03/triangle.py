#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 14:04
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : triangle.py
# @Software   : PyCharm
# @Description: 判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长：%f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积：%f' % area)
else:
    print('不能构成三角形')
