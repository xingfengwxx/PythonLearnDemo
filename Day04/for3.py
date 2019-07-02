#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 14:33
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : for3.py
# @Software   : PyCharm
# @Description: 用for循环实现1~100之间的偶数求和

sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)
