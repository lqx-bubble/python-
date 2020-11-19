# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class ImgsproPipeline(object):
#     def process_item(self, item, spider):
#         return item


#自己定义一个管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class imgsPipeline(ImagesPipeline):

    #可以根据图片地址进行图片数据的请求
    def get_media_requests(self, item, info):

        yield scrapy.Request(item['src'])

    #指定图片存储的路径
    def file_path(self, requests, response=None, info=None):    #requests 是scrapy.Request(item['src'])返回的对象
        imgName = requests.url.split('/')[-1]
        return imgName               #图片存储路径在setting 中设置


    #返回给下一个即将被执行的管道类
    def item_completed(self, results, item, info):
        return item
