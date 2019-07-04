#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 15:33
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : lily.py
# @Software   : PyCharm
# @Description: 找出100~999之间的所有水仙花数，
#               水仙花数是各位立方和等于这个数本身的数，
#               如：153 = 1 ** 3 + 5 ** 3 + 3 ** 3

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
