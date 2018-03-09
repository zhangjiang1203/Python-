import json

numbers = [2,3,4,5,6,7]

filename = 'number.json'
try:
    with open(filename,'w') as file_object:
        """函数json.dump() 接受两个实参:要存储的数据以及可用于存储数据的文件对象"""
        json.dump(numbers,file_object)
except FileNotFoundError:
    print("文件不存在")



"""读取json数据"""
try:
    with open(filename) as json_file:
        numbers = json.load(json_file)
except FileNotFoundError:
    print("该文件不存在")
print(numbers)

def get_stored_username():
    userfile = 'username.json'
    try:
        with open(userfile) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("你的名字：")
    userfilename = "username.json"
    with open(userfilename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("welcome to "+username)
    else:
        username = get_new_username()
        print("we'll remember you when you come back," + username + " .")
greet_user()