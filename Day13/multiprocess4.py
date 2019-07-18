#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/17 17:12
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : multiprocess4.py
# @Software   : PyCharm
# @Description: 


from time import time


def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()