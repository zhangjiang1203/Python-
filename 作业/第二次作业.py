#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 11:12 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : 第二次作业.py
# @Software: PyCharm

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}



if __name__ == "__main__":
    #把要获取的数据装入到一个列表中，每次循环的时候把下一级的数据添加到列表最后，
    # 取最后一个列表中的数据去匹配用户输入的数据，每次循环添加到列表中，每次去最后一个元素，
    # 返回上一层就是删除列表最后一个元素，
    current_menu = [menu]
    while True:
        if len(current_menu) == 0: break
        current_layer = current_menu[-1]
        if len(current_layer):
            for key in current_layer:
                print(key)
        else:
            print("没有更多数据了，骚年")
        #去除空格，全部小写
        message = input("请输入对应菜单(b返回上一层，q直接退出)：").strip().lower()
        if message == "b":
            #返回上一层，移除最后一个元素
            current_menu.pop()
            continue
        if message == "q":
            break
        if message not in current_layer:
            print("请输入上面显示的菜单，其他输入无效🤣🤣🤣🤣")
            continue
        #展示下层数据
        current_menu.append(current_layer[message])


