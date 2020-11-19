# -*- coding: utf-8 -*-
import scrapy
from imgsPro.items import ImgsproItem

class ZzimgSpider(scrapy.Spider):
    name = 'zzimg'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="container"]/div')
        for div in div_list:
        #  反爬机制：图片懒加载：当图片被滑动到可视界面时图片地址由   src2   变为   src
        #对应：使用伪属性  src2
            # src = div.xpath('./div/a/img/@src | ./div/a/img/@src2').extract_first()
            src = div.xpath('./div/a/img/@src2').extract_first()
            # print(src)

            item = ImgsproItem()
            item['src'] = src   #把src传给 item

            yield item