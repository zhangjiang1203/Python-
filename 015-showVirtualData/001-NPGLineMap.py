#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020-02-10 10:53 
# @Author : 张江 
# @Site :  
# @File : 001-NPGLineMap.py 
# @Software: PyCharm

import matplotlib.pyplot as plt
import pymysql
import matplotlib
import numpy as np
from matplotlib.font_manager import FontProperties  # 步骤一

font = FontProperties(fname="/System/Library/Fonts/STHeiTi light.ttc", size=14)  # 步骤二


#链接数据库获取对应的数据
def connectMyDataBase():
    connect = pymysql.connect(host='localhost',
                              user='root',
                              password='12345678',
                              database='ShowNPCDataModel',
                              port=3306,charset='utf8',
                              # cursorclass 设置返回的格式为数组套字典，不设置返回的就是元组套元组
                              cursorclass=pymysql.cursors.DictCursor)

    #获取游标，执行对应的sql语句
    cursor = connect.cursor()
    cursor.execute("select * from showNPCDataTable")
    res = cursor.fetchall()
    # print("获取的数据",res,type(res))

    # 最后关闭数据库
    cursor.close()
    connect.close()
    return res;


def drawLineWithData():
     res = connectMyDataBase()
     #处理数据
     total_list = []
     cure_list = []
     die_list = []
     date_list = []
     for data in res:
         date = data['date']
         date = date.strftime("%Y-%m-%d")
         date_list.append(date[5:])
         total_list.append(data["new_add"])
         cure_list.append(data['cure_num'])
         die_list.append(data['die_num'])

     # drawColumnView(date_list,total_list,cure_list,die_list)
     # drawLineChatView(date_list,total_list,cure_list,die_list)
     drawDetailNumView(date_list,total_list,cure_list,die_list)


#绘制折线图
def drawLineChatView(date_list,total_list,cure_list,die_list):
    x = date_list
    plt.plot(x, total_list, color='blue', label='新增人数', )
    plt.plot(x, cure_list, color='green', label='治愈人数')
    plt.plot(x, die_list, color='red', label='死亡人数')
    plt.xticks(rotation=-90)
    plt.xlabel('日期', fontproperties=font)
    plt.ylabel('人数', fontproperties=font)

    plt.title("新冠肺炎变化图", fontproperties=font)
    # 设置定义的字体，尤其是不支持中文的时候，图例使用中文时
    # 针对总人数 治愈人数死亡人数
    plt.legend(prop=font)
    plt.show()

#绘制柱状图
def drawColumnView(date_list,new_adds,cure_nums,die_nums):
    size = len(date_list)
    a = new_adds
    b = cure_nums
    c = die_nums
    x = np.arange(size)
    # 有多少个类型，只需更改n即可
    total_width, n = 4, 16
    width = total_width / n
    # 重新拟定x的坐标
    x = x - (total_width - width) / 2
    # 这里使用的是偏移
    plt.bar(x, a, width=width, label='新增人数')
    plt.bar(x + width, b, width=width, label='治愈人数')
    plt.bar(x + 2 * width, c, width=width, label='死亡人数')
    plt.legend(prop=font)
    # plt.xticks(x)
    plt.show()

def drawDetailNumView(date_list,new_adds,cure_nums,die_nums):
    size = len(date_list);
    a = new_adds
    b = cure_nums
    c = die_nums
    x = np.arange(size)

    total_width,n = 4,16;
    width = 0.3;
    #设置对应的坐标展示
    # 重新拟定x的坐标
    # x = x - (total_width - width) / 2

    fig,ax = plt.subplots()
    rect1 = ax.bar(x-width, a, width=width, label='新增人数')
    rect2 = ax.bar(x , b, width=width, label='治愈人数')
    rect3 = ax.bar(x+width , c, width=width, label='死亡人数')


    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('人数',fontproperties=font)
    ax.set_title('新冠肺炎变化图',fontproperties=font)
    ax.set_xticks(x)
    # ax.tick_params(labelsize=10)
    ax.set_xticklabels(date_list,rotation=-90)
    ax.legend(prop=font)
    #绘制数量
    addHeightNumber(ax,rect1)
    addHeightNumber(ax,rect2)
    addHeightNumber(ax,rect3)
    # plt.tick_params(labelsize=10)
    plt.show()


def addHeightNumber(ax,rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        #添加对应的展示文字信息
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=6)

if __name__ == '__main__':
    drawLineWithData()
