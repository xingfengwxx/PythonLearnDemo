#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/8/1 17:10
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : asyncio2.py
# @Software   : PyCharm
# @Description: async和await

import asyncio
import aiohttp


async def download(url):
    print('Fetch: ', url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(url, '--->', resp.status)
            print(url, '--->', resp.cookies)
            print('\n\n', await resp.text())


def main():
    loop = asyncio.get_event_loop()
    urls = [
        'https://www.baidu.com',
        'https://www.sohu.com/',
        'https://www.sina.com.cn/',
        'https://www.taobao.com/',
        'https://www.jd.com/'
    ]
    tasks = [download(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()