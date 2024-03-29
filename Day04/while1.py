#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 14:36
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : while1.py
# @Software   : PyCharm
# @Description: 猜数字游戏，计算出一个1~100之间的随机数由人来猜，计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入:'))
    if number < answer:
        print("大一点")
    elif number > answer:
        print("小一点")
    else:
        print('恭喜你猜对了！')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
