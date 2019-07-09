#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/9 10:06
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : vercode.py
# @Software   : PyCharm
# @Description: 生成指定长度的验证码（默认4个字符），由大小写英文字母和数字构成的随机验证码
import random


def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


if __name__ == '__main__':
    print('vercode:%s' % generate_code())
