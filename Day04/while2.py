#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 15:11
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : while2.py
# @Software   : PyCharm
# @Description: 用while循环实现1~100之间的偶数求和

sum, num = 0, 2
while num <= 100:
    sum += num
    num += 2
print(sum)
