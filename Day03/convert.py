#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 11:48
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : convert.py
# @Software   : PyCharm
# @Description: 英制单位英寸和公制单位厘米互换

value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == "cm" or unit == "厘米":
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效单位')
