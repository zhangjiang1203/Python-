import math

# magicians = ['dawei','lilin','wangdan']
# for magician in  magicians:
#     print(magician.title()+',that was a greate trick')
#     print("I cant‘t wati to see your next trick, " + magician.title()+"\n")
#
#
# print("Thank you ,everyone. That was a great magic show!")
#
# message = "hello Python world"
# print(message)
#
# pizzas = ['马铃薯','番茄','青椒']
# for pizza in pizzas:
#     print("我喜欢的pizza " + pizza)
# print("都是面做的pizza")


#使用range()函数 轻松地生成一系列的数字 range()只会生成指定的第一个值开始的数 输出不包含第二个值
for value in range(1,5):
    print(value)
#使用range() 时如果输出不符合预期 请尝试将指定的值加1或者减1
numbers  = list(range(1,6))
print(numbers)
#使用range()时还可以指定步长
event_numbers = list(range(2,11,2))
#函数range() 从2开始数 然后不断的加2 直到达到或者超过终值11
print(event_numbers)
squares = []
for value in range(1,100):
    # square = value ** 2
    squares.append(value)
print(squares)

#计算出数字列表的最大值和最小值
print(min(squares),max(squares),sum(squares))
#列表解析
mySquares = [value**2 for value in range(1,11)]
print(mySquares)
#切片
players = ["你","我","他","它","只有"]
print(players[0:3])
#提取列表的第2~4个元素
print(players[1:4])
#如果没有指定第一个索引，python将自动从头开始 同样的没有设置终止索引，python将从开始索引到最后
print(players[:2])
#负数索引返回离列表末尾相应距离的元素，
print(players[-3:])
for player in players[:3]:
    print(player)

#[:]是包含整个列表的切片，同时省略了起始索引和终止索引，即复制整个列表
my_foods = ['苹果','香蕉','梨','橘子']
friend_foods = my_foods[:]

#开始对复制的数组进行计算
my_foods.append('草莓')
friend_foods.append("柚子")
print('我喜欢的水果：')
print(my_foods)

print('我朋友喜欢的水果：')
print(friend_foods)
#列表直接赋值给列表的话 修改其中的一个列表，另一个也会跟着修改，这样就不是两个列表，只是将新变量关联到这个列表中，，
#这两个标量都指向同一个列表

all_foods = ['苹果','香蕉']#,'草莓','桔子','西瓜','柚子','板栗']
print(all_foods[0:3])
print(all_foods[-3:])
count = len(all_foods)
if count > 3:
   index = math.floor(count/2.0)
   print(all_foods[index-1:index+2])
