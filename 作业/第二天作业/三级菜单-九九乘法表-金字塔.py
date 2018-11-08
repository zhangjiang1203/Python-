#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 11:12 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : 三级菜单-九九乘法表-金字塔.py
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

def jiujiuMul():
    """
    九九乘法表
    :return:
    """
    for i in range(1,10):
        result = []
        for j in range(1,i+1):
            res = str(j) + "*" + str(i) + "=" + str(i*j)
            result.append(res)
        print(result)

def chooseMenu():
    # 把要获取的数据装入到一个列表中，每次循环的时候把下一级的数据添加到列表最后，
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
            print("\033[31m没有更多数据了，骚年\033[0m")
        # 去除空格，全部小写
        message = input("请输入对应菜单(b返回上一层，q直接退出)：").strip().lower()
        if message == "b":
            # 返回上一层，移除最后一个元素
            current_menu.pop()
            continue
        if message == "q":
            break
        if message not in current_layer:
            print("\033[31m请输入上面显示的菜单，其他输入无效🤣🤣🤣🤣\033[0m")
            continue
        # 展示下层数据
        current_menu.append(current_layer[message])

def jinzitaTest():
    """
    打印金字塔
    :param code: 输入金字塔层级
    :return:
    """
    while True:
        max_level = input("请金字塔层级,输入q退出>>>").strip()
        if max_level.lower() == "q": break
        if max_level.isdigit():
            level = int(max_level)
            for current_level in range(1,level+1):
                for i in range(level-current_level):
                    print(" ",end="")
                for j in range(2*current_level-1):
                    print("*",end="")
                print()
        else:
            print("\033[31m请输入序号\033[0m")





if __name__ == "__main__":

    while True:
        print("""
        1.九九乘法表
        2.三级菜单
        3.金字塔
        """)
        choice = input("请输入序号,输入q退出>>>").strip()
        if choice.isdigit():
            if int(choice) == 1:
                jiujiuMul()
            elif int(choice) == 2:
                chooseMenu()
            else:
                jinzitaTest()
        else:
            if choice.lower() == "q":break
            print("\033[31m请输入序号\033[0m")



