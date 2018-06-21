def getnum(x):
    y = 0
    while y <= x:
        yield y
        y += 1

#添加yeild关键字生成了一个生成器，
#函数中使用yeild会生成一个生成器对象
f = getnum(10)
#next函数每执行一次，都会把迭代器里面的数据移除一个
# print(type(f))
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(list(f))

#装饰器
'''
1.本身也是一个函数
2.增强被装饰函数的功能
'''

def decoration(func):
    def wrapper():
        print("开始输出")
        func()
        print("输出结束")
    return wrapper

@decoration
def show():
    print("这就是我说的：你们记住了没")
#执行显示的函数代码
show()

#当要被装饰的函数带有参数时，装饰器内部要添加有参数值
def decoration1(func):
    def wrapper(x):
        print('装饰器1')
        func(x)
        print('装饰器结束')
    return wrapper

@decoration1
def show1(name):
    print('输入的名字'+name)

show1('zhangsan')

#函数递归使用
def fact(n):
    if n <= 1:
        return 1;
    else:
        return n * fact(n-1)
# print(fact(3))

#斐波那契数列
def feibo(n):
    if n < 2:
        return 1
    else:
        # print(feibo(n-1)+feibo(n-2)+2)
        return feibo(n-1)+feibo(n-2)


l1 = [feibo(i) for i in range(0,11)]
print(l1)

'''
函数的设计规范
  耦合性：
     1.通过参数接受输入，以及通过return产生输出以保证函数的独立性
     2.尽量减少使用全局变量进行函数间通信
     3.不要在函数中修改可变类型的参数
     4.避免直接改变定义在另外一个模块中的变量
  聚合性：
     1.每个函数都应该有一个单一的、统一的目标，
     2.每个函数的功能都应该相对简单   
'''