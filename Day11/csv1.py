#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/12 15:02
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : csv1.py
# @Software   : PyCharm
# @Description: 读取CSV文件


import csv

filename = 'example.csv'
try:
    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print('无法打开文件：', filename)
else:
    for item in data:
        print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))
