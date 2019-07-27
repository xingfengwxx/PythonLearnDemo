#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/27 10:12
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : pdf.py
# @Software   : PyCharm
# @Description: 读取PDF文件

from PyPDF2 import PdfFileReader

with open('./res/Docker入门教程.pdf', 'rb') as f:
    reader = PdfFileReader(f, strict=False)
    print(reader.numPages)
    if reader.isEncrypted:
        reader.decrypt('')
    current_page = reader.getPage(5)
    print(current_page)
    print(current_page.extractText())