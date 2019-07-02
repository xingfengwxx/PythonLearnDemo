#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 10:47
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : circle.py
# @Software   : PyCharm
# @Description: 输入半径计算圆的周长和面积

import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)
