# -*- codeing = utf-8 -*-
# @Time : 2020/8/10 15:44
# @Author : 卢其鑫
# @File : 8.xpath解析-全国城市名称爬取.py
# @Software: PyCharm

#需求：解析出所有城市名称  https://www.aqistudy.cn/historydata/

import requests
from lxml import etree
if __name__ == '__main__':
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36'
    # }
    # url = 'https://www.aqistudy.cn/historydata/'
    # page_text = requests.get(url=url,headers=headers).text
    #
    # tree = etree.HTML(page_text)
    #
    # host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_names = []
    # #解析热门城市的城市名称
    # for li in host_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(hot_city_name)
    #
    # #解析全部城市名称
    # city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in city_names_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(city_name)
    #
    # print(all_city_names,len(all_city_names))



    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)
    #解析到热门城市和所有城市对应的a标签
    #热门： //div[@class="bottom"]/ul/li/a
    #所有： //div[@class="bottom"]/ul/div[2]/li/a
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)

    print(all_city_names,len(all_city_names))