#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/5 17:20
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : list3.py
# @Software   : PyCharm
# @Description: 
"""
生成列表
- 用range创建数字列表
- 生成表达式
- 生成器
"""
# 生成Fibonacci序列的生成器


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    # 用range创建数值列表
    list1 = list(range(1, 11))
    print(list1)
    # 生成表达式
    list2 = [x * x for x in range(1, 11)]
    print(list2)
    list3 = [m + n for m in 'ABCDEFG' for n in '12345']
    print(list3)
    print(len(list3))
    # 生成器（节省空间但生成下一个元素时需要花费时间）
    gen = (m + n for m in 'ABCDEFG' for n in '12345')
    print(gen)
    for elme in gen:
        print(elme, end=' ')
    print()
    gen = fib(20)
    for elme in gen:
        print(elme, end=' ')
    print()


if __name__ == '__main__':
    main()