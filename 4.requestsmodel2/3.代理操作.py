# -*- codeing = utf-8 -*-
# @Time : 2020/9/1 19:06
# @Author : 卢其鑫
# @File : 3.代理操作.py
# @Software: PyCharm

#需求：
import requests
url = 'https://www.baidu.com/s?&word=ip'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36'
    }
page_text = requests.get(url=url,headers=headers,proxies={"https":'115.221.240.203:9999'}).text
with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)

#反爬机制：封ip
#反反爬策略：使用代理ip发送请求