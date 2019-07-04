#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/4 14:59
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : function5.py
# @Software   : PyCharm
# @Description:
"""
函数的参数
- 位置参数
- 可变参数
- 关键字参数
- 命名关键字参数
"""
# 参数默认值
def f1(a, b=5, c=10):
    return a + 5 * 2 + c * 3


print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2, b=3, a=1))


# 可变参数
def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())


# 关键字参数
def f3(**kw):
    if 'name' in kw:
        print('欢迎你%s!' % kw['name'])
    elif 'tel' in kw:
        print('你的联系电话时：%s!' % kw['tel'])
    else:
        print('没找到你的个人信息')

param = {'name': '王星星', 'age': '25'}
f3(**param)
f3(name='王星星', age=25, tel='139 6666 8888')
f3(user='王星星', age=25, tel='139 6666 8888')
f3(name='王星星', age=25, mobile='139 6666 8888')
