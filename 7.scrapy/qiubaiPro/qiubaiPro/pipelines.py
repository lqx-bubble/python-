# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class QiubaiproPipeline(object):
    fp = None      # 文件为空
    #重写父类方法，该方法只在爬虫开始时被调用一次
    def open_spider(self,spider):
        print('开始爬虫。。。。。。')
        self.fp = open('./qiubai.txt','w',encoding='utf-8')

    #专门用来处理ite类型对象
    #该对象可以接收爬虫文件返回的item对象
    #该方法每接收一次item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        text = item['text']

        self.fp.write(author+':'+text+'\n')

        return item     #传递给下一个将会被执行的管道类


    def close_spider(self,spider):
        print('结束爬虫。。。。。。')
        self.fp.close()


#管道文件中一个管道类对应将一组数据存储到一个文件或一个载体当中
class pymysqlPileLine(object):
    coon = None
    cursor = None      #游标对象
    def open_spider(self,spider):
        self.coon = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='qiubai',charset='utf8')
    def process_item(self,item,spider):
        self.cursor = self.coon.cursor()

        try:
            self.cursor.execute('insert into qiubai values("%s","%s")'%(item["author"],item["text"]))
            self.coon.commit()    #没有异常，数据提交
        except Exception as e:    #出现异常，打印异常信息，回滚
            print(e)
            self.coon.rollback()
        return item         #传递给下一个将会被执行的管道类
    def close_spider(self,spider):
        self.cursor.close()
        self.coon.close()

