#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/13 15:34
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : asyncio1.py
# @Software   : PyCharm
# @Description: 异步I/O操作 - asyncio模块


import asyncio
import threading


@asyncio.coroutine
def hello():
    print('%s: hello, world!' % threading.current_thread())
    # 休眠不会阻塞主线程因为使用了异步I/O操作
    # 注意yield from才会等待休眠操作执行完成
    yield from asyncio.sleep(2)
    # asyncio.sleep(1)
    # time.sleep(1)
    print('%s: goodbye, world!' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 等待两个异步I/O操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
print('game voer!')
loop.close()
