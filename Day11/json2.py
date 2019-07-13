#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/13 11:09
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : json2.py
# @Software   : PyCharm
# @Description: 写入json文件


import json

teacher_dict = {'name': '白元芳', 'age': 25, 'title': '讲师'}
json_str = json.dumps(teacher_dict)
print(json_str)
print(type(json_str))
fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya']
json_str = json.dumps(fruits_list)
print(json_str)
print(type(json_str))