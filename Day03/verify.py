#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/2 11:15
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : verify.py
# @Software   : PyCharm
# @Description: 用户身份验证

username = input('请输入用户名：')
password = input('请输入口令：')
# 如果希望输入口令时，终端没有回显，可以使用getpass模块的getpass函数
# impor getpass
# password = getpass.getpass('请输入口令：')
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')
