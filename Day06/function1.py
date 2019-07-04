#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/4 13:52
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : function1.py
# @Software   : PyCharm
# @Description: 函数的定义和使用 - 计算组合数C(7,3)

# 将求阶乘功能封装成一个函数
def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


print(factorial(7) // factorial(3) // factorial(4))
