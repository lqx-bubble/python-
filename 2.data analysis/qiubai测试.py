# -*- codeing = utf-8 -*-
# @Time : 2020/9/25 22:53
# @Author : 泡影
# @File : qiubai测试.py
# @Software: PyCharm


import requests
from lxml import etree

headers = {
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
url = 'https://www.qiushibaike.com/text/'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
div_list =tree.xpath('//div[@class="col1 old-style-col1"]/div')
for div in div_list:
    author = div.xpath('./div[1]/a[2]/h2/text()')[0]
    text = div.xpath('./a[1]/div/span//text()')[0]
    print(author, text)