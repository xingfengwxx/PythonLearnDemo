#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/9 14:31
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : access.py
# @Software   : PyCharm
# @Description: 


class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == '__main__':
    main()
