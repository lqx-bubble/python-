# -*- coding: utf-8 -*-
import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.win4000.com/meinvtag3065.html']

    # 生成一个通用的url模板(不可变)
    url = 'http://www.win4000.com/meinvtag3065_%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('.//div[@class="list_cont Left_list_cont  Left_list_cont2"]//ul/li')
        for li in li_list:
            img_name = li.xpath('./a/p/text()').extract_first()
            # img_src = li.xpath('./a/img/@src').extract_first()   #图片地址动态加载，无法获取
            print(img_name)

        if self.page_num <= 5:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # 手动发送请求：callback回调函数专门用于数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)
