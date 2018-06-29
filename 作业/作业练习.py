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

# print(menu)

# menu1 = menu
# tag = True
# while tag:
#     for key1 in menu1:
#         print(key1)
#     choice1 = input('>>:')
#     if choice1 == 'b':
#         break
#     if choice1 == 'q':
#         tag = False
#         continue
#
#     if choice1 not in menu1:
#         continue
#
#     while tag:
#         #开始第二次输入
#         menu2 = menu1[choice1]
#         for key2 in menu2:
#             print(key2)
#         choice2 = input('>>:')
#         if choice2 == 'b':
#             break
#         if choice2 == 'q':
#             tag = False
#             continue
#         if choice2 not in menu2:
#             continue
#
#         while tag:
#             menu3 = menu2[choice2]
#             for key3 in menu3:
#                 print(key3)
#             choice3 = input('>>:')
#             if choice3 == 'b':
#                 break
#             if choice3 == 'q':
#                 tag = False
#                 continue
#             if choice3 not in menu3:
#                 continue
#
#             while tag:
#                 menu4 = menu3[choice3]
#                 for key4 in menu4:
#                     print(key4)
#                 choice4 = input('>>:')
#                 if choice4 == 'b':
#                     break
#                 if choice4 == 'q':
#                     tag = False
#                     continue
#                 if choice4 not in menu4:
#                     continue
#                 else:
#                     print('没有更多了退出吧骚年🤣🤣🤣🤣🤣🤣')





#利用数组 减少使用的次数
layers = [menu]
while True:
    if len(layers) == 0:break
    current_layer = layers[-1]
    for key in current_layer:
        print(key)
    choice = input('>>:').strip() #去掉空格
    if choice == 'b':
        layers.pop() #删除最后一个元素
        continue
    if choice == 'q':
        break        #退出循环
    if choice not in current_layer:
        continue
    layers.append(current_layer[choice])#数组中添加元素