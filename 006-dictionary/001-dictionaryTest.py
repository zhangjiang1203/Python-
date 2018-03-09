alien_0 = {'color':'green','points':5}
print(alien_0['color'])
new_points = alien_0['points']
print('you just earned ' + str(new_points) + " points")
#添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#定义一个空字典
alien_0['color'] = 'yello'
print(alien_0)

alien_1 = {'x_position':0,'y_position':25,'speed':'medium'}
print('Original x_position: ' + str(alien_1['x_position']))
#向右移动外星人
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_1['x_position'] = alien_1['x_position'] + x_increment
print(alien_1)

#删除键值对
del alien_0['points']
print(alien_0)


favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
print("Sarah's favorite language is "+favorite_languages['sarah'].title()+".")

user_info = {'first_name':'zhang',
             'last_name':'jiang',
             'age':17,
             'city':'shanghai'}

for key,value in user_info.items():
    print("\n key: "+ key + "  value:"+ str(value))

for key in sorted(user_info.keys()):
    print(key.title()+",thank you for taking the poll")

#创建一个用于存储外星人的空列表
aliens = []
#创建三十个外星人
for alien_number in range (0,30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
print(aliens)
#修改前5个数据的信息
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] =  10

#输出前五个外星人
for alien in aliens[0:5]:
    print(alien)


