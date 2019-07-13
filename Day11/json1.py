#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/13 11:01
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : json1.py
# @Software   : PyCharm
# @Description: 读取JSON数据


import json
import csv2

json_str = '{"name": "王星星", "age": 25, "title": "教授"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])


# 把转换得到的字典作为关键字参数传入Teacher构造器
teacher = csv2.Teacher(**result)
print(teacher)
print(teacher.name)
print(teacher.age)
print(teacher.title)