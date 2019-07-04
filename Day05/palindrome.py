#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/4 11:17
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : palindrome.py
# @Software   : PyCharm
# @Description: 判断输入的正整数是不是回文数，回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

num = int(input('请输入一个正整数：'))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)
