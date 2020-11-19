# -*- codeing = utf-8 -*-
# @Time : 2020/8/9 10:56
# @Author : 卢其鑫
# @File : 0.爬取图片.py
# @Software: PyCharm

import requests
if __name__ == '__main__':
    #如何爬取图片数据
    url = 'https://pic.qiushibaike.com/system/pictures/12344/123443932/medium/QDEWZUOD0WDPASOL.jpg'
    #  text(字符串)      content(二进制)      json() (对象)
    img_data = requests.get(url=url).content          #content返回的是图片的二进制数据

    with open('./qiutu.jpg','wb') as fp:
        fp.write(img_data)