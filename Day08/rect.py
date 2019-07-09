#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/9 14:49
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : rect.py
# @Software   : PyCharm
# @Description: 定义和使用矩形类


class Rect(object):
    """
    矩形类
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def perimeter(self):
        """

        Returns:周长

        """
        return (self.__width + self.__height) * 2

    def area(self):
        """

        Returns:面积

        """
        return self.__width * self.__height

    def __str__(self):
        """

        Returns:矩形对象的字符串表达式

        """
        return '矩形[%f,%f]' % (self.__width, self.__height)

    def __del__(self):
        """
        析构器
        Returns:

        """
        print('销毁矩形对象')


if __name__ == '__main__':
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(3.5, 4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())
