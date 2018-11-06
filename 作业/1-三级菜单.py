import os

#循环标识
tag = True
#存取文件名
file_name = 'account.txt'

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

#九九乘法表
def multiplicationtable():
    for i in range(1, 10):
        result = []
        for j in range(1, i + 1):
            value = str(j) + '*' + str(i) + '=' + str(i * j)
            result.append(value)
        print(result)



#金字塔
def pyramid():
    max_level = int(input('输入金字塔层级>>:').strip())
    for current_level in range(1,max_level+1):
        for i in range(max_level-current_level):
            print(' ',end='') #在一行中连续打印多个空格
        for j in range(2*current_level-1):
            print('*',end='') #在一行中连续打印多个*
        print()

def shoplist(user):
    product_list = [['Iphone7', 5800],
                    ['Coffee', 30],
                    ['iMac', 12000],
                    ['Python Book', 99],
                    ['Bike', 199],
                    ['ViVo X9', 2499]]
    shops_mark = {}
    tag = True
    while tag:
        for index,value in enumerate(product_list):
            print(index,value)
        market = input("输入商品编号选择商品，q退出>>:").strip()
        if market == 'q':
            tag = False
            continue

        if market.isdigit():
            index = int(market)
            if index < 0 or index >= len(product_list):
                continue
            balance = user['salary']
            product_name = product_list[index][0]
            product_price = product_list[index][1]
            if balance > product_price:
                # 添加到购物车中
                if product_name in shops_mark:
                    shops_mark[product_name]['count']+=1
                else:
                    shops_mark[product_name] = {"price":product_price,'count':1}
                # 更新用户金额信息
                users = getUseraccount()
                index = users.index(user)
                users.pop(index)
                user['salary'] = balance - product_price
                users.append(user)
                changAllAccount(users)
            else:
                print('对不起客官，您的余额不足，原价 {} 还差{}大洋，努力吧骚年🤣🤣🤣'.format(product_price,product_price-balance))

            print("""-------------------------已购买商品列表------------------------
                商品           单价          数量
                """)
            for k, v in shops_mark.items():
                print('%20s%13s%13s' % (k, v['price'], v['count']))
            print('账户余额===%s' % user['salary'])
            print('-' * 60)
        else:
            print('输入不合法')


def login():
    flag = True
    while flag:
        # 用户是否存在
        users = getUseraccount()
        for user in users:
            print(user)
        isexist = False
        account = input('请输入您的账号:')
        psw = input("请输入您的密码:")
        for user in users:
            if account in user.values():
                isexist = True
                loginCount = int(user['loginCount'])
                if loginCount == 3:
                    print('您登录密码输入错误次数过多，账号已被锁定')
                    flag = False
                    break
                #拿到对应的password和count值
                if psw == user['password']:
                    print('登录成功')
                    #输入工资，接下来选择商品
                    salary = input('请输入您的工资>>:').strip()
                    #重置用户登录次数并保存工资到对应的账号中
                    users.remove(user)
                    user['loginCount'] = 0
                    user['salary'] = int(salary)
                    users.append(user)
                    changAllAccount(users)
                    flag = False
                    #输出商品列表
                    shoplist(user)
                else:
                    loginCount+=1
                    #修改用户信息
                    users.remove(user)
                    user['loginCount'] = loginCount
                    users.append(user)
                    changAllAccount(users)
                    if loginCount == 3:
                        print('密码输入错误3次,账号已被锁定')
                        flag = False
                        break
                    else:
                        print('密码输入错误%s次,请重试' %loginCount)
                        break
        if not isexist:
            print('用户不存在，请重试')


def getUseraccount():
    #文件是否存在
    if os.path.isfile(file_name):
        with open(file_name, 'r+') as file_object:
            contents = file_object.readlines()
            users = []
            for line in contents:
                templine = line.strip()
                if not len(templine) or line.startswith('#'):
                    continue
                #字符串转字典
                users.append(eval(templine));
        return users
    else:
        # 文件不存在就创造文件
        print('生成账户文件')
        with open(file_name, 'a+') as object:
            users = [{'account': 'zhang', 'password': '123456', 'loginCount': 2,'salary':0},
                     {'account': 'wang', 'password': '123456', 'loginCount': 0,'salary':0},
                     {'account': 'guo', 'password': '123456', 'loginCount': 1,'salary':0},
                     {'account': 'xiang', 'password': '123456', 'loginCount': 0,'salary':0}]
            for value in users:
                account = str(value)
                object.write(account + '\n')
        return users

#存储修改用户的群组
def changAllAccount(account):
    with open(file_name, 'w+') as file_object:
        for value in account:
            user = str(value)
            file_object.write(user + '\n')


while tag:
    print('''
    0.三级菜单
    1.打印九九乘法表
    2.打印金字塔
    3.购物车
    ''')
    choice = input('>>:').strip()
    if choice == 'q' or choice == 'Q':
        break
    if choice.isdigit():
        choice = int(choice)
        if choice == 0:
            mulmenuoperation(menu)
        elif choice == 1:
            multiplicationtable()
        elif choice == 2:
            pyramid()
        else:
            # shoplist()
            login()
    else:
        print('输入不合法，请输入数字')
