# bicycles = ['trek','cannondale','redline','specialized']
# print(bicycles)
# print(bicycles[0])#列表是有序集合，可以访问他的位置或者索引
# #python为访问最后一个列表元素提供了一个特殊的语法 通过将索引值设置为-1 让python返回最后一个列表元素
# #同理 -2 返回倒数第二个元素 一次类推
# print(bicycles[-1])
# names = ['zhang san','li si','wangwu','zhao liu','lu qi']
# print(names)
# print("你好 " + names[1])
#
# bicycles.append('你好')#添加末尾元素
# print(bicycles)
# bicycles.insert(0,"中国")
# print(bicycles)
# del bicycles[0]
# print(bicycles)
# #pop() 删除列表末尾的元素 并让你能够接着使用它
# last_eleement = bicycles.pop()
# print(bicycles,last_eleement)
# #pop()加上索引可以删除任何位置的数据
# # bicycles.append("支付宝")
# # bicycles.append("微信")
# # print(bicycles)
# # bicycles.remove("微信")
# # print(bicycles)
# #排序 sort()对列表进行永久性排序 默认是按照字母顺序排序的,修改为相反元素的排列顺序时，设置reverse=True
# bicycles.sort(reverse=True)
# #sorted()函数对列表进行临时排序
# print(bicycles)

# placeArr = ['丽江','大理','哈尔滨','新疆','乌鲁木齐','厦门']
placeArr = ['lijiang','dali','haerbin','xinjiang','wulumuqi','xiamen']
print('原始顺序=='+str(placeArr))
# myList = placeArr.sort()
#默认的sorted 是按照字母顺序排序的
# print('sorted排序=='+str(sorted(placeArr,reverse=True)))
placeArr.reverse()
print('反转数组=='+str(placeArr))
placeArr.reverse()
print('再次反转数组=='+str(placeArr))
print('想去地方的个数=='+str(len(placeArr)))
#显示你的数组的个数 len(函数)

#showMsg = []#数组越界
#print(showMsg[-1])

# 列表赋值，对于多个值在一起的只想取其中的几个值，其他的可以用*_代替
x1,x2,*_ = [1,2,3,4,5,6,7,8,9,0]
print(x1,x2)
# 正向步长
showList = ["nihao","jiushi","haole","haiyou","nikanzhe","meishile"]
#倒着取值，从第三个元素开始倒着取值，翻转列表直接设置从最后一个开始取值就可以了
short = showList[3::-1]
short1 = showList[::-1]
print(short)


#使用匿名函数,这就是一个表达式，不是一个语句
f1 = lambda x,y:x+y
print(f1(5,6))
l3 = [(lambda x:x*2),(lambda x:x*3)]
for i in l3:
    #对l3中的lambda表达式进行赋值，对l3中的元素进行遍历，每个lambda语句进行赋值
    #第一个赋值为4，第二个也赋值为4
    #得到的结果为 8 12
    print(i(4))


l4 = [0,1,2,3,4,5,6]
def add(x,y):
    return x + y;
# print(reduce(add,l4))
# # print(l4.reduce())
# mylist =  [j**2 for j in range(1,11)]
#
# for i in [j**2 for j in range(1,11)]:
#     print(i)

# list =  [lambda j: j**2  for j in range(1,5)]
# print(list[0](6))
#
# for i in [lambda j: j**2  for j in range(1,5)]:
#     #添加lambda表达式，并对他进行赋值操作,存储的表达式，对传入的参数进行平方操作
#     print(i(2))

f = open('a.txt','r',encoding='utf-8')
data = f.read()#一次获取所有的数据
# 默认打开模式就是r
'''打开文本模式
r 只读，没有文件会报错
w 只写，没有文件会创建文件，存在会覆盖之前的所有内容
a 追加模式，不存在则创建，存在则追加类容

在每个模式后面添加+模式表示可以同时读取

非文本文件只能使用b模式，b模式是表示使用字节的方式操作，所有的文件都是以字节的方式存放在磁盘中
b模式方式打开时读取到的是字节类型，写入时也要提供字节类型，不能指定编码


根据句柄拿到文件内容
f.read()  读取所有类容，光标移动到文件末尾
f.readline() 读取一行内容，光标移动到第二行首部
f.readlines() 读取每一行内容，存放在列表中

f.readable() 文件是否可读
f.writeable() 文件是否可写
f.closed() 文件是否关闭
f.encoding()
f.flush()  立刻将文件类容从内存刷到硬盘中

'''
