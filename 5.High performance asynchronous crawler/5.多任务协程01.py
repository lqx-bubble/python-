# -*- codeing = utf-8 -*-
# @Time : 2020/8/15 11:03
# @Author : 卢其鑫
# @File : 5.多任务协程01.py
# @Software: PyCharm

import asyncio
import time

async def requests(url):
    print('正在下载',url)
    #time.sleep(2)                      #在异步协程中如果出现了同步模块相关代码，将无法实现异步
    await asyncio.sleep(2)           #当在asyncio中遇到阻塞操作必须进行手动挂起
    print('下载完毕',url)

start = time.time()
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.doubanjia.com'
]

#任务列表：存放多个任务对象
stasks = []
for url in urls:
    c = requests(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)

loop = asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))

print(time.time()-start)