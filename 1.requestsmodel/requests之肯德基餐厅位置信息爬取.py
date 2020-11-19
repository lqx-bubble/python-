# -*- codeing = utf-8 -*-
# @Time : 2020/8/8 14:27
# @Author : 卢其鑫
# @File : requests之肯德基餐厅位置信息爬取.py
# @Software: PyCharm



import requests
import json

if __name__ == '__main__':

    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    word = input('enter a citi:')
    param = {
        'cname':'',
        'pid':'',
        'keyword': word,
        'pageIndex': '1',
        'pageSize': '10'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome / 84.0.4128.3Safari / 537.36'
    }
    response = requests.get(url=url, params=param, headers=headers)

    list_data = response.json()

    fileName = word + '肯德基餐厅位置.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)

    print('---over!!!')
