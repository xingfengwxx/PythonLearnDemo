#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/18 9:33
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : singlethread1.py
# @Software   : PyCharm
# @Description: 不使用多线程的情况 - 模拟多个下载任务
from random import randint
from time import sleep, time


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('下载完成！耗费了%d秒' % time_to_download)


def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()