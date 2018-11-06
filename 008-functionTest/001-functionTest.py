
# import make_pizza
# make_pizza.make_pizza(16,"pep",'zh','jiang')

#通过make_pizza 导入make_pizza函数
from make_pizza import make_pizza
make_pizza(16,"pep",'zh','jiang')

#as给指定的函数指定别名
#from make_pizza import make_pizza as make

#as给指定模块指定别名
import make_pizza as make
make.make_pizza(19,'jj','haha')

def greet_user(username):
    """显示简单的问候语"""
    print("hello,world "+username)

greet_user("zhangjiang")

#def 关键字声明这是个函数 greent_user是一个函数名 username是一个参数 定义以冒号结尾
#后面的所有缩进构成了函数体
#调用函数 直接写上函数名

def display_message():
    print("开始学习函数")

display_message()

def favorite_book(title):
    print('one of my favorite books is '+title)

favorite_book("my love")

def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print("\n I have a "+animal_type + ".")
    print("My " +animal_type + "'s name is " + pet_name.title()+".")

describe_pet("动物","猪")

#关键字实参
describe_pet(animal_type='pig',pet_name='tom')

def get_formatted_name(first_name,last_name):
    full_name = first_name + last_name
    return full_name.title()

# while True:
#     print("\nplace tell me your name:")
#     print("\nenter ‘q’ at any time to quit")
#     f_name = input("First_name:")
#     if f_name == "q":
#         break;
#     l_name = input("Last_name:")
#     if l_name == "q":
#         break;
#     f_name = get_formatted_name(f_name,l_name)
#     print("\n hello,"+f_name)

#向列表中的每个人发送一个消息
def greet_user(names):
    for name in names:
        msg = "Hello, "+ name.title()+"."
        print(msg)

userNames = ['hahaha','zhang','jiang']
greet_user(userNames[:])

#传递任意数量的实参
def make_pizza(*topping):
    """打印顾客的所有的配料"""
    print(topping)
make_pizza('zhangjiang','lisi','wanger')

#一个*号创建一个空的元祖 两个**创建一个空字典形参

#调用一个函数模块
#使用嵌套函数 内层函数调用外层函数中的变量，系统会自动记忆外层函数变量，
x = 5

def test1(name):
    name = name + 1
    print(name)
print(x)
#传入的参数值没有改变

l1 = [1,2,3]
def test2(myList):
    myList.pop()
    print(myList)

# test2(l1)
# print(l1)
#不可变对象 不论在函数中怎么修改 都不会影响他原本的值
#list 是一个可变对象，在函数中传入一个可变对象，并修改它，对象也会被修改，

def test3(myList):
    myList.pop()
    print(myList)
#传入list的时候，传入的是一个对象的切片，相当于重新生成一个对象，修改这个对象不影响原来的值
test3(l1[:])
print(l1)

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
# print(l4.reduce())
mylist =  [j**2 for j in range(1,11)]

for i in [j**2 for j in range(1,11)]:
    print(i)

for i in [lambda j: j**2  for j in range(1,5)]:
    #添加lambda表达式，并对他进行赋值操作
    print(i(2))

