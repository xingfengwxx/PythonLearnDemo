#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/9 10:52
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : lottery.py
# @Software   : PyCharm
# @Description: 双色球随机选号程序

from random import randrange, randint, sample


def display(balls):
    """

    Args:
        balls:

    Returns:输出列表中的双色球号码

    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=" ")
    print()


def random_select():
    """

    Returns:随机选一组号码

    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    for _ in range(6):
        index = randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index]
    # 上面的for循环也可以写成下面这行代码
    # sample函数是random模块下的函数
    # selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注：'))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()