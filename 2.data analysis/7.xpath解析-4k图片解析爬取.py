# -*- codeing = utf-8 -*-
# @Time : 2020/8/10 13:19
# @Author : 卢其鑫
# @File : 7.xpath解析-4k图片解析爬取.py
# @Software: PyCharm

#需求：解析下载图片数据  http://pic.netbian.com/4kmeinv/

import requests
from lxml import etree
import os
import time
from multiprocessing.dummy import Pool


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36'
}

start_time = time.time()

def get_page():
    url = 'http://pic.netbian.com/4kmeinv/index_%d.html'
    for pageNum in range(2, 20):
        new_url = format(url % pageNum)
        response = requests.get(url=new_url, headers=headers)
        page_text = response.text

        # 数据解析: src的属性值  和alt属性值
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="slist"]/ul/li')
        save(li_list)

#创建一个文件夹
def save(li_list):
    if not os.path.exists('./4ktuopian(模块分页)'):
        os.mkdir('./4ktuopian(模块分页)')
    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        # 通用处理中文乱码的解决方案
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')

        # print(img_name,img_src)

        #持久化存储
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = '4ktuopian(模块分页)/' + img_name

        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '   ---下载成功！！！')

    print('over!!!')
# pool = Pool(5)
# pool.map(get_page)
get_page()
end_tiem = time.time()
print(end_tiem-start_time)