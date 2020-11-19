# -*- codeing = utf-8 -*-
# @Time : 2020/10/3 20:09
# @Author : 泡影
# @File : ceshi.py
# @Software: PyCharm


from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://baidu.com')

print(driver.title)