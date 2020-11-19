# -*- codeing = utf-8 -*-
# @Time : 2020/8/10 17:06
# @Author : 卢其鑫
# @File : 爬取站长素材中免费简历模板.py
# @Software: PyCharm

#需求：爬取站长素材中免费建立模板
import requests
from lxml import etree
import os

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36'
    }

    fp = open('zhanzhangsucai.txt', 'w', encoding='utf-8')

    url = 'http://sc.chinaz.com/jianli/free_%d.html'
    for pageNum in  range(2,11):
        new_url = format(url%pageNum)

        page_text = requests.get(url=new_url,headers=headers).text
        tree = etree.HTML(page_text)
        a_list = tree.xpath('//div[@id="main"]//a[@class="title_wl"]/@href')
        title_list = tree.xpath('//div[@id="main"]//a/text()')
        #print(a_list)

        for a in a_list:
            #print(a)
            detail_rul = a
            detail_text = requests.get(url=detail_rul,headers=headers).text
            detail_tree = etree.HTML(detail_text)
            detail_a_list = detail_tree.xpath('//div[@class="clearfix mt20 downlist"]/ul[@class="clearfix"]/li/a/@href')[0]
            fp.write(detail_a_list+'\n')

            print(detail_a_list)
    print('---over!!!')




