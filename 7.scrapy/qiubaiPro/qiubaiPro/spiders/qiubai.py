# -*- coding: utf-8 -*-
import scrapy
from qiubaiPro.items import QiubaiproItem      #基于管道存储，导入items类


#基于终端指令持久化存储
class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']



# 基于终端指令持久化存储
#     def parse(self, response):
#         #解析作者的名称和段子的内容（全部）
#         div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
#         all_data = []     #存储所有解析到的数据
#         for div in div_list:
#             # extract() 可以将selector 中参数data存储的字符串提取出来
#             # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
#             author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
#             # 列表调用 extract()之后，表示将selector中的每一个data中的字符串提取出来
#             text = div.xpath('./a[1]/div/span//text()').extract()
#             text = "".join(text)    #将列表转为字符串
#             dic = {
#                 'author':author,
#                 'text':text
#             }
#
#             all_data.append(dic)
#
#             # print(author,text)
#             # print(all_data)
#         return all_data



#基于管道持久化存储

    def parse(self, response):
        #解析作者的名称和段子的内容（全部）
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in div_list:
            # extract() 可以将selector 中参数data存储的字符串提取出来
            # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            author = div.xpath('./div[1]/a[2]/h2/text() | ./div[1]/span/h2/text()').extract_first()
            # 列表调用 extract()之后，表示将selector中的每一个data中的字符串提取出来
            text = div.xpath('./a[1]/div/span//text()').extract()
            text = "".join(text)    #将列表转为字符串

            item = QiubaiproItem()     #实例化一个item对象
            #封装到item中
            item['author'] = author
            item['text'] = text

            yield item   #将item提交给管道