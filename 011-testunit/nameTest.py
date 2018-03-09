from name_function import get_formatted_name

print("输入 ‘q’ 退出")
while True:
    first = input("请输入你的姓：")
    if first == "q":
        break
    last = input("请输入你的名字：")
    if last == "q":
        break
    formatted_name = get_formatted_name(first,last)
    print("输入的名字是：==" + formatted_name)