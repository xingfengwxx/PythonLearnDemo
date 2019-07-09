#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/8 16:19
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : dict2.py
# @Software   : PyCharm
# @Description: 字典的操作

def main():
    stu = {'name':'王星星', 'age':25, 'gender':True}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())
    for elme in stu.items():
        print(elme)
        print(elme[0], elme[1])
    if 'age' in stu:
        stu['age'] = 20
    print(stu)
    stu.setdefault('score', 60)
    print(stu)
    stu.setdefault('score', 100)
    print(stu)
    stu['score'] = 100
    print(stu)


if __name__ == '__main__':
    main()
