#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 15:19
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : for6.py
# @Software   : PyCharm
# @Description: 打印各种三角形图片

row = int(input('请输入行数：'))
for i in range(row):
    for _ in range(i + 1):
        print("*", end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print("*", end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
