#定义一个输入输出的函数
def writefilecontent():
    circel = True
    responses = []
    while circel:
        print("请开始输入")
        print("退出请输入Q或q")

        f_name = input("请输入您的姓名：")
        f_place = input("请输入您的出生地：")

        responses.append(f_name + " " + f_place)
        f_quit = input("是否还要继续:请输入是或否")
        if f_quit == 'q' or f_quit == 'Q':
            circel = False

    return responses



filename = "writefile.txt"
with open(filename,"w") as file_object:

    myMessage = writefilecontent()
    messgeStr = ''
    for name in myMessage:
        messgeStr += name + '\n'
    print(messgeStr)
    file_object.write(messgeStr)

#open file函数的中的参数
"""
Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default) 只读
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
"""
"""try-except处理可能引发的异常"""

print("输入两个数字，求他们的商是多少")
print("输入q退出")
while True:
    first_num = input("first number:")
    if first_num == 'q':
        break
    second_num = input("second number:")
    if second_num == 'q':
        break

    try:
        answer = int(first_num)/int(second_num)
    except ZeroDivisionError:
        print("被除数不能为0")
    else:
        print(answer)
