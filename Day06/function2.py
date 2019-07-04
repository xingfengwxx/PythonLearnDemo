#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/4 14:13
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : function2.py
# @Software   : PyCharm
# @Description: 函数的定义和使用 - 求最大公约数和最小公倍数

def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1

def lcm(x, y):
    return x * y // gcd(x, y)

print(gcd(15, 27))
print(lcm(15, 27))
