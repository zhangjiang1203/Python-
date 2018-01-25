cars = ['audi','bmw','subaru','toyoa']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#python是区分大小写的
age = 18
if age > 0 and age < 20:
    print(age)
else:
    print('age不合适')

#使用or检查
if age > 0 or age < -100:
    print(age)
else:
    print('age不合适')

banned_users = ['andrew','carolina','david','line']
user = 'marie'
if user not in banned_users:
    print(user.title()+",you can post a response if you wish")

age = 17
if age > 17:
    print("你的年纪可以投票了")
    print("你有注册过投票吗？")
else:
    print("对不起，你的年纪还不能参与选票")
    print('请等到18岁再来参加')

child_age = 12
if age < 6:
    print('你可以免费进')
elif age < 18:
    print('你需要花费5元')
else:
    print('你需要花费10元')

alien = 'red'
alien_color = ['green','yellow','red']
if alien == 'green':
    print("你杀死了一个"+alien+"外星人，获取了五个积分点")
elif alien == 'yellow':
    print("你杀死了一个" + alien + "外星人，获取了十个积分点")
else:
    print("你杀死了一个" + alien + "外星人，获取了十五个积分点")


#练习测试
current_users = ['Tom','jhon','mei','daxiong','nina']
new_users = ['xiaoming','dingna','tom','jhon','wanger']

change_user = []
for old in current_users:
    change_user.append(old.lower())

for user in new_users:
    if user in change_user:
        print(user + '  老用户加一分')
    else:
        print(user + '  这是个新用户')

