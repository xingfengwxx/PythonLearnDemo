#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 14:31
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : for2.py
# @Software   : PyCharm
# @Description: 用for循环实现1~100之间的偶数求和

sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)
