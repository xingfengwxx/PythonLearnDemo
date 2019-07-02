#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 11:03
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : strings.py
# @Software   : PyCharm
# @Description: 字符串常用操作

str1 = 'hello, world!'
print('字符串的长度是：', len(str1))
print('单词首字母大写：', str1.title())
print('字符串变大写：', str1.upper())
# str1 = str1.upper()
print('字符串是不是大写：', str1.isupper())
print('字符串是不是以hello开头：', str1.startswith('hello'))
print('字符串是不是以hello结尾：', str1.endswith('hello'))
print('字符串是不是以感叹号开头：', str1.startswith('!'))
print('字符串是不是以感叹号结尾：', str1.endswith('!'))
str2 = '- \u738b\u661f\u661f'
str3 = str1.title() + ' ' + str2.lower()
print(str3)
