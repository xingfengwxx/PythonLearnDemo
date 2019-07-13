#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/13 10:41
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : ex2.py
# @Software   : PyCharm
# @Description: 异常机制 - 处理程序在运行时可能发生的状态


input_again = True
while input_again:
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        print('%d / %d = %f' % (a, b, a / b))
        input_again = False
    except (ValueError, ZeroDivisionError) as msg:
        print(msg)