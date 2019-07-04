#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/4 14:33
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : function4.py
# @Software   : PyCharm
# @Description:
"""
Python常用模块
- 运行时服务相关模块: copy / pickle / sys / ...
- 数学相关模块: decimal / math / random / ...
- 字符串处理模块: codecs / re / ...
- 文件处理相关模块: shutil / gzip / ...
- 操作系统服务相关模块: datetime / os / time / logging / io / ...
- 进程和线程相关模块: multiprocessing / threading / queue
- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
- Web编程相关模块: cgi / webbrowser
- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...
"""
import shutil
import time
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)

shutil.copy('D:/PycharmProjects/PythonLearnDemo/Day01/hello.py', 'C:/Users/WangXingxing/Desktop/first.py')
os.system('ls -l')
os.chdir('C:/Users/WangXingxing/Desktop')
os.system('ls -l')
os.mkdir('test')