#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 10:38
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : centigrade.py
# @Software   : PyCharm
# @Description: 将华氏温度转为摄氏温度 F = 1.8C + 32

f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
