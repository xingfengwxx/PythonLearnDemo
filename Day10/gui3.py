#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/11 9:35
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : gui3.py
# @Software   : PyCharm
# @Description: 使用tkinter创建GUI
# - 在窗口上制作动画


import tkinter
import time


# 播放动画效果的函数
def play_animation():
    canvas.move(oval, 2, 2)
    canvas.update()
    top.after(50, play_animation)


x = 10
y = 10
top = tkinter.Tk()
top.geometry('600x600')
top.title('动画效果')
top.resizable(False, False)
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, 600, 600, fill='gray')
oval = canvas.create_oval(10, 10, 60, 60, fill='red')
canvas.pack()
top.update()
play_animation()
tkinter.mainloop()