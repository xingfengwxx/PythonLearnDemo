#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 15:12
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : for5.py
# @Software   : PyCharm
# @Description: 输入两个正整数计算最大公约数和最小公倍数

x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('%d和%d的最大公约数是%d' % (x, y, factor))
            print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
            break
