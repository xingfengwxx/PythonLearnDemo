#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/4 15:14
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : function6.py
# @Software   : PyCharm
# @Description: 作用域问题

# 局部作用域
def foo1():
    a = 5


foo1()


# 局部作用域
b = 10


def foo2():
    print(b)


foo2()


def foo3():
    b = 100      # 局部变量
    print(b)


foo3()
print(b)


def foo4():
    global b
    b = 200      # 全局变量
    print(b)


foo4()
print(b)
