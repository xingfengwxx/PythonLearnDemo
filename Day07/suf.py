#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/9 10:12
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : suf.py
# @Software   : PyCharm
# @Description: 获取文件名的后缀名


def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


if __name__ == '__main__':
    print(get_suffix(input('filename=')))
