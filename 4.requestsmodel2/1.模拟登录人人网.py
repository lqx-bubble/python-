# -*- codeing = utf-8 -*-
# @Time : 2020/8/11 16:15
# @Author : 卢其鑫
# @File : 1.模拟登录人人网.py
# @Software: PyCharm

import requests
from lxml import etree
from codeclass import FateadmApi

#封装识别验证码的函数
def TestFunc(File_name,pred_Type):
    pd_id           = "125303"     #用户中心页可以查询到pd信息
    pd_key          = "GLwe6VYlla6W0jpS+ClJtx14eGKGy679"
    app_id          = "325303"     #开发者分成用的账号，在开发者中心可以查询到
    app_key         = "3jknHy1VOQR0V5ppaI4imOiqyqlaOMdH"
    #识别类型，
    #具体类型可以查看官方网站的价格页选择具体的类型，不清楚类型的，可以咨询客服
    pred_type       = pred_Type
    api             = FateadmApi(app_id, app_key, pd_id, pd_key)
    # 查询余额
    balance 		= api.QueryBalcExtend()   # 直接返余额
    # api.QueryBalc()
    # 通过文件形式识别：
    file_name       = File_name
    # 多网站类型时，需要增加src_url参数，具体请参考api文档: http://docs.fateadm.com/web/#/1?page_id=6
    # result =  api.PredictFromFileExtend(pred_type,file_name)   # 直接返回识别结果
    rsp             = api.PredictFromFile(pred_type, file_name)  # 返回详细识别结果
    return file_name


#对验证码图片进行捕获和识别
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36'
    }
url = 'http://www.renren.com/SysHome.do'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
code_img_data = requests.get(url=code_img_src,headers=headers).content
with open('.code,jpg','wb') as fp:
    fp.write(code_img_data)

#使用打码平台识别验证码
result = TestFunc('code.jpg',30400)
print(result)