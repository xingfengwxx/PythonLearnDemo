#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/13 14:46
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : test3.py
# @Software   : PyCharm
# @Description: 不良内容过滤

import re


def main():
    sentence = '你丫是傻叉吗？我操你大爷的。Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)


if __name__ == '__main__':
    main()

