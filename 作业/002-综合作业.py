import os

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

def shoplist():
    markets = {
        'apple': 10,
        'tesla': 100000,
        'mac': 3000,
        'lenovo': 30000,
        'chicken': 10,
    }

#编辑用户
file_name = 'account.txt'

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
                flag = int(user['loginCount'])
                if flag == 3:
                    print('您登录密码输入错误次数过多，账号已被锁定')
                    flag = False
                    break
                #拿到对应的password和count值
                if psw == user['password']:
                    print('登录成功')
                    #重置用户登录次数
                    users.remove(user)
                    user['loginCount'] = 0
                    users.append(user)
                    changAllAccount(users)
                    flag = False
                    break
                else:
                    flag+=1
                    #修改用户信息
                    users.remove(user)
                    user['loginCount'] = flag
                    users.append(user)
                    changAllAccount(users)
                    if flag == 3:
                        print('密码输入错误3次,账号已被锁定')
                        flag = False
                        break
                    else:
                        print('密码输入错误%s次,请重试' %flag)
                        break;
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




tag = True
while tag:
    print('''
    1.打印九九乘法表
    2.打印金字塔
    3.购物车
    ''')
    choice = input('>>:').strip()
    if choice == 'q' or choice == 'Q':
        break
    choice = int(choice)
    if choice == 1:
        multiplicationtable()
    elif choice == 2:
        pyramid()
    else:
        login()




