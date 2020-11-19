# -*- codeing = utf-8 -*-
# @Time : 2020/8/8 10:52
# @Author : 卢其鑫
# @File : requests之百度翻译破解.py
# @Software: PyCharm


import requests
import json

if __name__ == '__main__':
    #1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome / 84.0.4128.3Safari / 537.36'
    }
    #3.post请求参数处理（和get请求一致）
    word = input('enter a word:')
    data = {
        'kw':word
    }
    #4.请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    #5.获取相应数据:josn()方法返回的是obj   (如果确认响应数据是josn类型的才可以使用josn())
    dic_obj = response.json()
    print(dic_obj)
    #6.持久化存储
    fileName = word+'翻译结果.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)

    print('---over!!!')