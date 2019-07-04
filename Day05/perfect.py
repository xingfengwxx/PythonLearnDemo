#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/4 10:38
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : perfect.py
# @Software   : PyCharm
# @Description: 找出1~9999之间的所有完美数
#               完美数是除自身外其他所有因子的和正好等于这个数本身的数
#               例如：6 = 1 + 2 +3， 28 = 1 + 2 + 4 + 7 + 14

import math

for num in range(1, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor
    if sum == num:
        print(num)
