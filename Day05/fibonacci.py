#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/4 10:54
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : fibonacci.py
# @Software   : PyCharm
# @Description: 输出斐波那契数列的前20个数：1，1,2,3,5,8,13,21...

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
