#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/4 17:03
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : list1.py
# @Software   : PyCharm
# @Description: 
"""
定义和使用列表
- 用下标访问元素
- 添加元素
- 删除元素
"""

def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    print(fruits)
    # 通过下标访问元素
    print(fruits[0])
    print(fruits[1])
    print(fruits[-1])
    print(fruits[-2])
    # print(fruits[-5]) # IndexError
    # print(fruits[4]) # IndexError
    fruits[1] = 'apple'
    print(fruits)
    # 添加元素
    fruits.append('pitaya')
    fruits.insert(0, 'banana')
    print(fruits)
    # 删除元素
    del fruits[1]
    fruits.pop()
    fruits.pop(0)
    fruits.remove('apple')
    print(fruits)

if __name__ == '__main__':
    main()