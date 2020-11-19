# -*- codeing = utf-8 -*-
# @Time : 2020/8/11 20:59
# @Author : 卢其鑫
# @File : 2.线程池基本使用.py
# @Software: PyCharm


# import time
# #使用单线程串行方式执行
# def get_page(str):
#     print("正在下载 ：",str)
#     time.sleep(2)
#     print('下载成功：',str)
#
# name_list =['xiaozi','aa','bb','cc']
#
# start_time = time.time()
#
# for i in range(len(name_list)):
#     get_page(name_list[i])
#
# end_time = time.time()
# print('%d second'% (end_time-start_time))


import time
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
#使用线程池方式执行
start_time = time.time()
def get_page(str):
    print("正在下载 ：",str)
    time.sleep(3)
    print('下载成功：',str)

name_list =['xiaozi','aa','bb','cc','dd','ee','ff','gg','hh','ii','11','12']

#实例化一个线程池对象
pool = Pool(4)
#将列表中每一个列表元素传递给get_page进行处理。  第一个参数get_page是阻塞参数，第二个参数name_list是可迭代参数
pool.map(get_page,name_list)
pool.close()
pool.join()
end_time = time.time()
print(end_time-start_time)