#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/13 10:54
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : ex4.py
# @Software   : PyCharm
# @Description: 引发异常和异常栈


def f1():
    raise AssertionError('发生异常')


def f2():
    f1()


def f3():
    f2()


f3()
