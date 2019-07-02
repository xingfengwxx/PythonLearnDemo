#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 10:12
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : variable2.py
# @Software   : PyCharm
# @Description: 使用input函数输入，使用int()进行类型转换，使用占位符格式化输出的字符串

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
