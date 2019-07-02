#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 14:52
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : ninenine.py
# @Software   : PyCharm
# @Description: 输出乘法口诀表（九九表）

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
