#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/5 17:44
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : set1.py
# @Software   : PyCharm
# @Description: 定义和使用集合

def main():
    set1 = {1, 2, 3, 3, 2, 1}
    print(set1)
    print('Length =', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)
    set2.discard(5)
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍历集合器
    for elem in set2:
        print(elem ** 2, end=' ')
    print()
    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)


if __name__ == '__main__':
    main()