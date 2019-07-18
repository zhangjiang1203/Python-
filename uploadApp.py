#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 16:43
# @Author  : 张江
# @Site    : 
# @File    : uploadApp.py
# @Software: PyCharm


import os,time
#用于发送http请求到蒲公英，第三方模块，需要pip install requests来下载
import requests
#用于打开浏览器，并打开某个网址，系统自带模块
import webbrowser
#传入的dir就是文件夹A的路径，如果你的脚本就在当前路径，直接传入“.”即可
def IpaCreatedLastly(dir):
    Dirdic={}#key＝文件夹名称（包含IPA的文件夹路径），value＝创建的时间
    for i in os.listdir(dir):  #查找文件夹A中所有的文件
        if os.path.isdir(i):
            # 算出每个文件夹的创建时间，这里的时间是指距离1970年一月一日的秒数，所以数值越大越说明是最新创建的
            creattime=os.path.getctime(dir+os.sep+i)
            Dirdic[i]=creattime
            # 按value值（创建的时间）从大到小对字典排序
    Dirdic=sorted(Dirdic.items(),key=lambda item:item[1],reverse=True)
    # 字典排列的第一的key值，即最新创建的文件夹
    DirCreatedLastly=Dirdic[0][0]
    print('要上传的文件目录是：'+DirCreatedLastly)
    IpaPath=""
    # 找到该文件路径下面的IPA文件
    for i in os.listdir(dir+os.sep+DirCreatedLastly):
        if(i.find('.ipa')!=(-1)):
            # 得到最新打包的IPA的夹路径
            IpaPath=dir+os.sep+DirCreatedLastly+os.sep+i
            return IpaPath
    return IpaPath

def uploadIPA(IPAPath):
    if(IPAPath==''):
        print('未找到对应上传的IPA文件!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return
    else:
        url='http://www.pgyer.com/apiv1/app/upload'         #上传的url地址
        data={
            'uKey':'你自己的userkey',
            '_api_key':'你自己的apikey',
            'installType':'2',
            'password':'123456',
            'updateDescription':'测试服'
            }                                #发送的参数数据
        files={'file':open(IPAPath,'rb')}       #上传的文件
        r=requests.post(url,data=data,files=files)   # 发送post请求。完事。。。。

def openDownloadUrl():
    webbrowser.open(r'你自己的蒲公英下载链接',new=1,autoraise=True)


if __name__ == '__main__':
    dir = "."
    ipaPath = IpaCreatedLastly(dir)
    uploadIPA(ipaPath)
    openDownloadUrl()