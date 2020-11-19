# -*- codeing = utf-8 -*-
# @Time : 2020/8/16 17:36
# @Author : 卢其鑫
# @File : 4.动作链和iframe的处理.py
# @Software: PyCharm

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains     #导入动作链对应的链
bro = webdriver.Chrome(executable_path='chromedriver.exe')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#如果定位的标签是存在在于iframe中的，则必须通过如下操作进行标签定位
bro.switch_to.frame('iframeResult')   #iframeResult是想要定位的iframe标签的id
div = bro.find_element_by_id('draggable')

#动作链
action = ActionChains(bro)              #实例化
action.click_and_hold(div)              #点击并长按指定的标签

for i in range(5):
    action.move_by_offset(17,1).perform()             #  共5次，每次水平移动17个像素    perform()  表示立即执行
    sleep(0.7)

action.release()        #释放动作链

sleep(5)
bro.quit()      #关闭浏览器