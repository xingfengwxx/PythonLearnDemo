#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 11:54
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : rolldice.py
# @Software   : PyCharm
# @Description: 掷骰子决定做什么事情

from random import randint

face = randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲冷笑话'
print(result)
