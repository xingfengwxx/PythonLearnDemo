#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 15:02
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : for4.py
# @Software   : PyCharm
# @Description: 输入一个正整数判断它是不是素数

from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
