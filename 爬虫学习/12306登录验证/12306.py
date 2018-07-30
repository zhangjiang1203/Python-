# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:张江

import requests
import config

'''
1.访问登录页面获取cookie
session = requests.Session()
session.get(url)
2.下载验证码图片 # https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.6080874721933833
result = session.get(url)
result即为图片信息
3.校验验证码 # https://kyfw.12306.cn/passport/captcha/captcha-check
session.post(url,data=params)
4.校验用户名和密码 https://kyfw.12306.cn/passport/web/login
session.post(url,data=params)
'''


# 获取验证码图片
# https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.6080874721933833
# 验证点击验证码是否正确
# https://kyfw.12306.cn/passport/captcha/captcha-check
# post请求参数为，answer是点击时的坐标显示位置
'''
answer:input('请输入验证码图片序号>>:')
answer: 116,57,217,52
login_site: E
rand: sjrand
'''

# 开始登录
# https://kyfw.12306.cn/passport/web/login
# 登录的参数
'''
"username": "896884@qq.com"
"password": "sfsdfds"
"appid": "otn"
'''

# 定义一个坐标字典，添加对应的坐标
codeDict = {
    '1':'37,46',
    '2':'111,46',
    '3':'181,46',
    '4':'254,46',
    '5':'37,116',
    '6':'111,116',
    '7':'181,116',
    '8':'254,116',
}

def getCodeLocation(index):
    indexs = index.split(',')
    codes = []
    for item in indexs:
        codes.append(codeDict[item])

    return ','.join(codes);



print(getCodeLocation('2,8'))