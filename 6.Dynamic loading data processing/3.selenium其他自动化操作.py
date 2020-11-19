# -*- codeing = utf-8 -*-
# @Time : 2020/8/16 16:57
# @Author : 卢其鑫
# @File : 3.selenium其他自动化操作.py
# @Software: PyCharm

from time import sleep
from selenium import webdriver

bro = webdriver.Chrome(executable_path='chromedriver.exe')

bro.get('https://www.taobao.com/')

#标签定位(定位搜索框)
search_input = bro.find_element_by_id('q')
#搜索框输入
search_input.send_keys('Iphone')

#执行一组js程序(让页面滚动)
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)

#点击搜索按钮
btn = bro.find_element_by_css_selector('.btn-search')
btn.click()

bro.get('https://www.baidu.com')
sleep(2)
#回退
bro.back()
sleep(2)
#前进
bro.forward()


sleep(5)

bro.quit()      #关闭浏览器