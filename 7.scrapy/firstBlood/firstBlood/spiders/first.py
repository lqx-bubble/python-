# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    #爬虫文件名称：唯一标识
    name = 'first'
    #允许的URL名：限定start_urls中哪些URL可以进行请求的发送
    # allowed_domains = ['www.baidu.com']
    #起始的URL列表：该列表中存放的URL会被scrapy自动发送请求
    start_urls = ['https://www.baidu.com/','https://www.sogou.com']

    #用作于数据解析：response 表示请求成功后对应的响应对象
    def parse(self, response):
       print(response)
