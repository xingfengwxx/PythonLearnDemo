#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/9 10:36
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : yanghui.py
# @Software   : PyCharm
# @Description: 输出10行的杨辉三角 - 二项式的n次方展开系数
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# ... ... ...


def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
