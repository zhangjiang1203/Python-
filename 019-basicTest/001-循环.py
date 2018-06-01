

a = 4
b = 5
print(a==b)

l1 = ['x','y','z']
print(a == l1)
l2 = ['x','y','z']
print(l1 == l2)
# None始终都是假的
print('x' in l1)
URL = 'www.baidu.com'
while URL:
    print(URL)
    URL = URL[1:]
#循环中添加,号 可以不用换行显示
#break跳出最内层循环
#continue 调到所处的最近层循环的开始处
#pass 占位语句
#else代码块 循环常终止才会执行，如果循环终止
#是由break跳出导致的，则else不会执行

sum = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i = i + 1
else:
    print("game over==" + str(sum))


d1 = {'x':1,'y':23,'z':78}
for key in d1.keys():
    print(key)

l3 = [0,1,2,3,4,5,6]
l4 = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
d2 = {}
while l3:
    d2[str(len(l3)-1)] = l4[len(l3)-1]
    l3.pop()
else:
    print("game over===%@", d2)

#zip 取得一个或者多个序列为参数，将给定的序列中的并排元素
#配成元祖，返回这些元祖的列表
#当参数长度不同时，zip会以最短序列的长度为准
l5 = [1,2,3,4,5,6,7,8]
l6 = ['a','b','c','d','e','f','g','h']
name = zip(l5,l6)
print(list(name))
#动态构建字典
d = {}
for (k,v) in zip(l5,l6):
    d[k] = v
print(d)

# 增加对象引用计数的场景
# 1.对象创建
# 2.将对象添加进容器
# 3.对象被当做参数传递给函数
# 4.为对象创建另外的变量名

# 减少引用计数
# 1.引用此对象的某些变量名被显示销毁 如 del x
# 2.给引用此对象的某变量名重新赋值
# 3.从容器中移除对象时，类似 list.pop()
# 4.容器本身被销毁时

l7 = [1,2,3]
l8 = [ i** 2 for i in l7]
print(l8)
l9 = [ i**2 for i in l7 if i > 3]
print(l9)

l10 = [(i,j) for i in l7 for j in l1 ]
print(l10)
