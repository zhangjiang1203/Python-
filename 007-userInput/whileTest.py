count_number = 1
while count_number <= 5:
    print(count_number)
    count_number += 1

# message = "\n Tell me something, and I will repeat it back to you:"
# message += "\n Enter 'quit' to end the program."
# inputMessage = ""
# while inputMessage != 'quit':
#     inputMessage = input(message)
#     if inputMessage != 'quit':
#         print(inputMessage)


# ticket = "\n 请输入观众的年龄，输入quit之后退出:"
# message = ""
# while message != 'quit':
#     message = input(ticket)
#     if message == 'quit':
#         break;
#     count = int(message)
#     if count < 3 :
#         print("您可以免费观影")
#     elif count >= 3 and count <=12:
#         print("您的观影费用为10元")
#     else:
#         print("您的观影费用为15元")

# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
# #输出所有被验证的用户
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
#
#
# #删除一个列表中的重复的对象
# pets = ['cat','cat','cat','cat','dog','rabbit','goldfish']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

responses = {}
#设置一个标志，支出调查是否继续
polling_active = True
while polling_active:
    name = input("\n请输入你的名字?:")
    response = input("\n 你比较喜欢爬那座山?:")
    #存储信息
    responses[name] = response
    #看看是否还有人要参与调查
    repeat = input("\n你是否还想让其他人参与调查(是或否)")
    if repeat == '否':
        polling_active = False
#输出调查结果
print("\n---poll results---")
for name,response in responses.items():
    print(name+"喜欢爬"+response + ".")