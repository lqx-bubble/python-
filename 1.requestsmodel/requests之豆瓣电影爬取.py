# -*- codeing = utf-8 -*-
# @Time : 2020/8/8 13:52
# @Author : 卢其鑫
# @File : requests之豆瓣电影爬取.py
# @Software: PyCharm

import requests
import json

if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list?'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '0',      #从库中的第1部电影开始去取
        'limit': '20'       #一次取出的部数
    }
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome / 84.0.4128.3Safari / 537.36'
    }
    response = requests.get(url=url,params=param,headers=headers)

    list_data = response.json()

    fp = open('douban.json', 'w', encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print('---over!!!')