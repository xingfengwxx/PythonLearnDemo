#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/13 16:58
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : generator2.py
# @Software   : PyCharm
# @Description: 生成器 - 使用yield关键字


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n += 1


for x in fib(20):
    print(x)
