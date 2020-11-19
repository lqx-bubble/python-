#!/usr/bin/python
# -*- coding:utf8 -*-


from lxml import etree
if __name__ == '__main__':
    # 实例化好了一个etree对象，且将被解析的源码加载到该对象中
    tree = etree.parse('text.html')

    # r = tree.xpath('/html/body/div')
    # r = tree.xpath('/html//div')
    # r = tree.xpath('//div')       #  //可以表示多个层级 或 表示从任意位置开始定位。

    # r = tree.xpath('//div[@class="song"]')     #定位所有 class='song' 的div

    # r = tree.xpath('//div[@class="song"]/p[3]')     #定位所有 class='song' 的div里的第3个p标签

    # r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0]      #取到 class="tang" 的div 里的第5个li 标签里的a 标签里的文本，[0]表示把列表转成字符串。

    # r = tree.xpath('//li[7]//text()')[0]        #//text() 获取标签中非直系的文本内容（所有的文本内容）

    # r = tree.xpath('//div[@class="tang"]//text()')

    r = tree.xpath('//div[@class="song"]/img/@src')     #取 img 标签里的 src 属性值

    print(r)