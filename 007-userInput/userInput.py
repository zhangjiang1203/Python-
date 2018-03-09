
name = input('请输入你的名字：')
print('hello, '+name+' !')
age = input('请输入你的年龄：')
print(age)
num = input("请输入数字:")
print('转换前：' + num)
num = int(num)
num += 3
print("转换后："+ str(num))

carMessage = input("你需要租赁什么样的汽车:")
print("let me see if I can find you a Subaru")

eatNum = input("请输入用餐人数:")
eatNum = int(eatNum)
if eatNum > 8:
    print("非常抱歉，这里没有空桌")
else:
    print("这里有空桌")
num = input("请输入一个数字:")
num = int(num)
if num % 10 == 0:
    print(str(num)+ "是10的整数倍")
else:
    print(str(num) + "不是10的整数倍")