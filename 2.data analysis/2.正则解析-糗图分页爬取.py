# -*- codeing = utf-8 -*-
# @Time : 2020/8/9 15:47
# @Author : 卢其鑫
# @File : 2.正则解析-糗图分页爬取.py
# @Software: PyCharm


import requests
import re
import os
import time

#需求：爬取糗事百科中糗图板块下所有的糗图图片
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome / 84.0.4128.3Safari / 537.36'
    }

    #创建一个文件夹，保存所有的图片
    if not os.path.exists('./qiutuLibs（多页）'):
        os.mkdir('./qiutuLibs（多页）')

    #设置一个通用的url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    start_time = time.time()
    for pageNum in  range(1,14):
        new_url = format(url%pageNum)

        #使用通用爬虫对url对应的整张页面进行爬取
        page_text = requests.get(url=new_url,headers=headers).text


        #使用聚焦爬虫将页面中所有的糗图进行解析/提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex,page_text,re.S)
        #print(img_src_list)
        for src in img_src_list:
            #拼接出一个完整的图片url
            src = 'https:'+src
            #请求到图片的二进制数据
            img_data = requests.get(url=src,headers=headers).content
            #生成图片名称
            img_name = src.split('/')[-1]
            #图片存储路径
            imgPath = './qiutuLibs（多页）/'+img_name
            with open(imgPath,'wb') as fp:
                fp.write(img_data)
                print(img_name,'---下载成功！！！')
        print('---over!!!')

    end_time = time.time()
    print(end_time-start_time)