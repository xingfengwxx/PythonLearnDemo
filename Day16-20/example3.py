#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/29 14:31
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : example3.py
# @Software   : PyCharm
# @Description: 

"""
函数递归调用 - 函数直接或者间接的调用了自身
1. 收敛条件
2. 递归公式
n! = n * (n-1)!
f(n) = f(n-1) + f(n-2)
1 1 2 3 5 8 13 21 34 55 ...
"""

from contextlib import contextmanager
from time import perf_counter


def fac(num):
    """
    求阶乘
    Args:
        num:

    Returns:

    """
    assert num >= 0
    if num in (0, 1):
        return 1
    return num * fac(num - 1)


def fib2(num):
    """
    普通函数
    Args:
        num:

    Returns:

    """
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


# 动态规划 - 保存可能进行重复运算的中间结果（空间换时间）
def fib(num, results={}):
    """
    斐波拉切数
    Args:
        num:
        results:

    Returns:

    """
    assert num > 0
    if num in (1, 2):
        return 1
    try:
        return results[num]
    except KeyError:
        results[num] = fib(num - 1) + fib(num - 2)
        return results[num]


@contextmanager
def timer():
    try:
        start = perf_counter()
        yield
    finally:
        end = perf_counter()
        print(f'{end - start}秒')


def main():
    """
    主函数
    Returns:

    """
    # for val in fib3(20):
    #     print(val)
    # gen = fib3(20)
    # for _ in range(10):
    #     print(next(gen))
    for num in range(1, 121):
        with timer():
            print(f'{num}: {fib(num)}')
    # print(fac(5))
    # print(fac(-5))


if __name__ == '__main__':
    main()