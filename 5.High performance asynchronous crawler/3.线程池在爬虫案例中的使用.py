# -*- codeing = utf-8 -*-
# @Time : 2020/8/11 21:30
# @Author : 卢其鑫
# @File : 3.线程池在爬虫案例中的使用.py
# @Software: PyCharm


#需求：爬取梨视频的视频数据
import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool

headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome / 84.0.4128.3Safari / 537.36'
    }

#原则：线程池处理的是阻塞且较为耗时的操作

#对下述url发起请求解析出视频详情页的url和视频名称
url = 'https://www.pearvideo.com/category_2'
page_text = requests.get(url=url,headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls = []     #存储所有视频的链接和名字
for li in li_list:
    detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    # print(detail_url,neme)
    #对详情页的url发起请求
    detail_page_text = requests.get(url=detail_url,headers=headers).text
    #从详情页解析出视频的url
    ex = 'srcUrl="(.*?)",vdoUrl'
    video_url = re.findall(ex,detail_page_text)[0]
    # print(video_url)
    dic = {
        'name':name,
        'url':video_url
    }
    urls.append(dic)

def get_video_data(dic):
    url = dic['url']
    print(dic['name'],'正在下载...')
    data = requests.get(url=url,headers=headers).content
    #持久化存储操作
    with open(dic['name'],'wb') as fp:
        fp.write(data)
        print(dic['name'],'下载成功！！！')
#使用线程池对视频数据进行请求（较为耗时的阻塞操作）
pool = Pool(4)
pool.map(get_video_data,urls)

pool.close()
pool.join()