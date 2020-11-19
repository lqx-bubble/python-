#!/usr/bin/python
# -*- coding:utf8 -*-

#需求：爬取58二手房中的房源信息

import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36'
    }
    #爬取到页面源码数据
    url = 'https://nn.58.com/ershoufang/'
    page_text = requests.get(url=url,headers=headers).text

    #数据解析
    tree = etree.HTML(page_text)    #实例化对象
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')        #  li_list 存储的就是li标签对象
    fp = open('58.txt','w',encoding='utf-8')
    for li in li_list:
        #页面局部解析
        title = li.xpath('./div[2]/h2/a/text()')[0]
        fp.write(title + '\n')
        print(title)