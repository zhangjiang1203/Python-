file_name = 'account.txt'
def login():
    flag = 0
    users = getUseraccount()
    print(users)
    while flag < 3:
        account = input('请输入您的账号:')
        psw = input("请输入您的密码:")

        for user in users:
            if account in user.values():
                #返回当前的索引号
                index = users.index(user);
                #拿到对应的password和count值
                flag = users[index]['loginCount']
                if flag == 3:
                    print('您登录密码输入过多，账号已被锁定')
                    break
                if psw == users[index]['password']:
                    print('登录成功')
                else:
                    flag+=1
                    print('密码输入错误')
                    break
            else:
                print('账号不存在请重新输入')
                break


#编辑用户
def getUseraccount():

    with open(file_name,'a+') as object:
        temp = object.readline()
        users = []
        for value in temp:
            users.append(eval(value));
        if len(users) == 0:
            users = [{'account': 'zhang', 'password': '123456', 'loginCount': 2},
                     {'account': 'wang', 'password': '123456', 'loginCount': 0},
                     {'account': 'guo', 'password': '123456', 'loginCount': 1},
                     {'account': 'xiang', 'password': '123456', 'loginCount': 0}]
            for value in users:
                account = str(value)
                object.write(account + '\n')
        return users
login()