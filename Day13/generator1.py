#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/13 16:51
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : generator1.py
# @Software   : PyCharm
# @Description: 生成器 - 生成器语法


seq = [x * x for x in range(10)]
print(seq)

gen = (x * x for x in range(10))
print(gen)
for x in gen:
    print(x)

num = 10
gen = (x ** y for x, y in zip(range(1, num), range(num - 1, 0, -1)))
print(gen)
n = 1
while n < num:
    print(next(gen))
    n += 1

