#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/8 15:11
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : dict1.py
# @Software   : PyCharm
# @Description: 定义和使用字典

def main():
    scores = {'王星星':95, '白元芳':78, '狄仁杰':82}
    print(scores['王星星'])
    print(scores['狄仁杰'])
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    print(scores.get('武则天', 60))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('王星星', 100))
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()
