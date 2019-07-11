#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/11 9:44
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : turtle1.py
# @Software   : PyCharm
# @Description: 用turtle模块绘图
# 这是一个非常有趣的模块 它模拟一只乌龟在窗口上爬行的方式来进行绘图


import turtle


turtle.pensize(3)
turtle.penup()
turtle.goto(-180, 150)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.pendown()
turtle.begin_fill()
for _ in range(36):
    turtle.forward(200)
    turtle.right(170)
turtle.end_fill()
turtle.mainloop()