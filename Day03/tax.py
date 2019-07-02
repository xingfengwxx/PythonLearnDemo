#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 14:11
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : tax.py
# @Software   : PyCharm
# @Description: 输入月收入和五险一金计算个人所得税

salary = float(input('本月收入：'))
insurance = float(input('五险一金：'))
diff = salary - insurance - 5000
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 36000:
    rate = 0.03
    deduction = 0
elif diff < 144000:
    rate = 0.1
    deduction = 2520
elif diff < 300000:
    rate = 0.2
    deduction = 16920
elif diff < 420000:
    rate = 0.25
    deduction = 31920
elif diff < 660000:
    rate = 0.3
    deduction = 52920
elif diff < 960000:
    rate = 0.35
    deduction = 85920
else:
    rate = 0.45
    deduction = 181920
tax = abs(diff * rate - deduction)
print('个人所得税：￥%.2f元' % tax)
print('实际到手收入：￥%.2f元' % (diff + 5000 - tax))
