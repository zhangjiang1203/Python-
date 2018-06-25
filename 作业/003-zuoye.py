import os


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

#编辑用户
file_name = 'account.txt'
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
            users = [{'account': 'zhang', 'password': '123456', 'loginCount': 2},
                     {'account': 'wang', 'password': '123456', 'loginCount': 0},
                     {'account': 'guo', 'password': '123456', 'loginCount': 1},
                     {'account': 'xiang', 'password': '123456', 'loginCount': 0}]
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

#开始登录
login()

'''
文件I/O操作的时候，使用a+模式读取不出文件的内容，不指定模式或者r,r+就可以读出文件内容，
不管是什么模式都是已经获取到文件，为什么读取不出文件的内容

'''