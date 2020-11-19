# -*- codeing = utf-8 -*-
# @Time : 2020/8/17 13:00
# @Author : 卢其鑫
# @File : 5.模拟登录qq空间.py
# @Software: PyCharm

from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='chromedriver.exe')

bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')      #切换作用域    (iframe)

a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()                                       #点击切换账号密码登录

userName_tag = bro.find_element_by_id('u')      #定位到账号输入框
passWord_tag = bro.find_element_by_id('p')      #定位到密码输入框
sleep(1)

userName_tag.send_keys('2580942497')            #输入QQ号
sleep(1)
passWord_tag.send_keys('20000618luqixin')        #输入密码
sleep(1)

btn = bro.find_element_by_id('login_button')
btn.click()                                         #点击登录

sleep(7)

bro.quit()


