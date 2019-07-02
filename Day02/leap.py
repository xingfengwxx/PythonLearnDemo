#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 10:52
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : leap.py
# @Software   : PyCharm
# @Description: 输入年份，如果是闰年输出True，否则输出False

year = int(input('请输入年份：'))
# 如果代码太长写成一行不便于阅读，可以使用\或（）拆行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
