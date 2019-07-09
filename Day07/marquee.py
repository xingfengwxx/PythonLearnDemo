#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/8 16:30
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : marquee.py
# @Software   : PyCharm
# @Description: 在屏幕上显示跑马灯文字
import os
import time


def main():
    str = '北京欢迎你为你开天辟地......'
    while True:
        print(str)
        time.sleep(0.2)
        str = str[1:] + str[0:1]
        # for Windows use os.system('cls') instead
        os.system('cls')


if __name__ == '__main__':
    main()
