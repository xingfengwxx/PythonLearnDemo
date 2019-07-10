#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/9 19:33
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : association.py
# @Software   : PyCharm
# @Description: 对象之间的关联关系


from math import sqrt


class Point(object):


    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


    def move_to(self, x, y):
        self._x = x
        self._y = y