# -*- codeing = utf-8 -*-
# @Time : 2020/8/17 16:19
# @Author : 卢其鑫
# @File : 6.谷歌无头浏览器+反检测.py
# @Software: PyCharm

from selenium import webdriver
from time import sleep
from selenium.webdriver import ChromeOptions        #实现规避检测
from selenium.webdriver.chrome.options import Options     #实现无可视化界面的操作


#实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


#实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])


#实现 无可视化 以及 让selenium规避被检测风险
bro = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options, options=option)

bro.get('https://www.baidu.com')

print(bro.page_source)
sleep(2)
bro.quit()