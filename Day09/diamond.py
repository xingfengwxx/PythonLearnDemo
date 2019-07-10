#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/9 19:25
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : diamond.py
# @Software   : PyCharm
# @Description: 多重继承
# - 菱形继承(钻石继承)
# - C3算法(替代DFS的算法)

class A(object):

    def foo(self):
        print('foo of A')


class B(A):
    pass


class C(A):

    def foo(self):
        print('foo of C')


class D(B, C):
    pass


class E(D):

    def foo(self):
        print('foo in E')
        super().foo()
        super(B, self).foo()
        super(C, self).foo()


if __name__ == '__main__':
    d = D()
    d.foo()
    e = E()
    e.foo()