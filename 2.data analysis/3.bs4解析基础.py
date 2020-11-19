# -*- codeing = utf-8 -*-
# @Time : 2020/8/9 16:15
# @Author : 卢其鑫
# @File : 3.bs4解析基础.py
# @Software: PyCharm

from bs4 import BeautifulSoup
if __name__ == '__main__':
    #将本地的html文档中的数据加载到该对象中
    fp = open('./text.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    #print(soup)
    #print(soup.a)                  #  soup.标签   返回的是html中出现的第一次标签

    #print(soup.find('a'))           #  soup.find('标签') == soup.标签

    #print(soup.find('div',class_= 'song'))      #  soup.find('div',class_= 'song')   属性定位

    #print(soup.find_all('a'))               #soup.find_all('标签')    返回的是所有符合要求的标签（列表）

    #print(soup.select('某种选择器（id/class/标签 等）'))

    #print(soup.select('.tang > ul > li > a')[0])        #返回tang里的ul里的li里的第一个a标签     （>） 表示一个层级  （空格）表示多个层级    '.tang > ul > li > a' == '.tang > ul a'

    #print(soup.a.text)    #  soup.标签.text/string/get_text()        获取标签里的文本数据
                           # text/get_text():  可以获取该标签下所有的文本内容
                           # string: 只可以获取该标签下直系的文本内容

    #print(soup.a['herf'])     #获取a标签下href内容