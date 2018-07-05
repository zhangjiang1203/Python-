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



# tag=True
# while tag:
#     menu1=menu
#     for key in menu1: # 打印第一层
#         print(key)
#
#     choice1=input('第一层>>: ').strip() # 选择第一层
#
#     if choice1 == 'b': # 输入b，则返回上一级
#         break
#     if choice1 == 'q': # 输入q，则退出整体
#         tag=False
#         continue
#     if choice1 not in menu1: # 输入内容不在menu1内，则继续输入
#         continue
#
#     while tag:
#         menu_2=menu1[choice1] # 拿到choice1对应的一层字典
#         for key in menu_2:
#             print(key)
#
#         choice2 = input('第二层>>: ').strip()
#
#         if choice2 == 'b':
#             break
#         if choice2 == 'q':
#             tag = False
#             continue
#         if choice2 not in menu_2:
#             continue
#
#         while tag:
#             menu_3=menu_2[choice2]
#             for key in menu_3:
#                 print(key)
#
#             choice3 = input('第三层>>: ').strip()
#             if choice3 == 'b':
#                 break
#             if choice3 == 'q':
#                 tag = False
#                 continue
#             if choice3 not in menu_3:
#                 continue
#
#             while tag:
#                 menu_4=menu_3[choice3]
#                 for key in menu_4:
#                     print(key)
#
#                 choice4 = input('第四层>>: ').strip()
#                 if choice4 == 'b':
#                     break
#                 if choice4 == 'q':
#                     tag = False
#                     continue
#                 if choice4 not in menu_4:
#                     continue
#
#                 # 第四层内没数据了，无需进入下一层

# 九九乘法表
def multiplicationtable():
    for i in range(1, 10):
        result = []
        for j in range(1, i + 1):
            value = str(j) + '*' + str(i) + '=' + str(i * j)
            result.append(value)
        print(result)

def pyramid():
    theCode = 5
    for  i in  range(theCode+1):
        for j in range(theCode - i):
            print(" ", end='')
            # 输出相应的空格
        for i_temp in range(2*i-1):
            print('*', end='')
            # 正向输出字母
        print()

def mulmenuoperation(mylist):
    # 利用数组 减少使用的次数
    layers = [mylist]
    while True:
        if len(layers) == 0: break
        current_layer = layers[-1]
        if len(current_layer):
            for key in current_layer:
                print(key)
        else:
            print('骚年，没有更多菜单了😂😂😂😂😂')
        print()
        choice = input('输入b返回上一层，q退出，输入菜单进入下一层>>:').strip()  # 去掉空格
        if choice == 'b':
            layers.pop()  # 删除最后一个元素
            continue
        if choice == 'q':
            break  # 退出循环
        if choice not in current_layer:
            print('骚年，要输入打印出来的菜单😂😂😂😂😂')
            continue
        layers.append(current_layer[choice])  # 数组中添加元素

mulmenuoperation(menu);


# max_level=5
# for current_level in range(1,max_level+1):
#     for i in range(max_level-current_level):
#         print(' ',end='') #在一行中连续打印多个空格
#     for j in range(2*current_level-1):
#         print('*',end='') #在一行中连续打印多个空格
#     print()