#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/12 15:07
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : csv2.py
# @Software   : PyCharm
# @Description: 写入CSV文件


import csv


class Teacher(object):

    def __init__(self, name, age, title):
        self.__name = name
        self.__age = age
        self.__title = title
        self.__index = -1

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def title(self):
        return self.__title


filename = 'teacher.csv'
teachers = [Teacher('王星星', 25, '教授'), Teacher('狄仁杰', 22, '打工仔')]

try:
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for teacher in teachers:
            writer.writerow([teacher.name, teacher.age, teacher.title])
except BaseException as e:
    print('无法写入文件：', filename)
else:
    print('保存数据完成！')