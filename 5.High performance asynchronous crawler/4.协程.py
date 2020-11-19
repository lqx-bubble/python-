# -*- codeing = utf-8 -*-
# @Time : 2020/8/15 10:11
# @Author : 卢其鑫
# @File : 4.协程.py
# @Software: PyCharm

import asyncio

async def requests(url):
    print('正在请求的url是',url)
    print('请求成功',url)
    return url
#async 修饰的函数，调用之后返回的一个协程对象
c = requests('https://www.baidu.com/')

# #创建一个事件循环对象
# loop = asyncio.get_event_loop()
# #将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)


# #task的使用
# loop = asyncio.get_event_loop()
# #基于loop创建一个task对象
# task = loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)


# #future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)


#绑定回调
def callback_func(task):
    #result()返回的就是任务对象中封装的协程对象对应的函数返回值
    print(task.result())

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
#将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)