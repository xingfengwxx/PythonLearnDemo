#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/9 10:17
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : findmax.py
# @Software   : PyCharm
# @Description: 找出最大或最小的元素


def max1():
    fruits = ['grape', 'apple', 'strwberry', 'waxberry', 'pitaya']
    # 直接使用内置的max和min函数找出列表中最大和最小元素
    # print(max(fruits))
    # print(min(fruits))
    max_value = min_value = fruits[0]
    for index in range(1, len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]
        elif fruits[index] < min_value:
            min_value = fruits[index]
    print('Max:', max_value)
    print('Min:', min_value)


def max2(x):
    """

    Args:
        x:

    Returns:列表中最大和第二大的元素的值

    """
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


if __name__ == '__main__':
    max1()
    print(max2([1, 2, 3, 4, 5, 6, 7]))
