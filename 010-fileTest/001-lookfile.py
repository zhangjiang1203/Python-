#python在当前文件下查找这个文件，分为绝对路径和相对路径
#关键字with是为了让python妥善的打开和关闭文件
with open('pi_mycircle.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())

pi = ''
for line in contents:
    pi+= line.rstrip()

print(pi.strip())

file_name =  "learningpython.txt"
try:
    with open(file_name) as file_read:
       messages = file_read.read()
       print(messages)
except FileNotFoundError:
    msg = 'sorry,the file ' + file_name + " does not exist."
    print(msg)

messageStr = ""
for message in messages:
    messageStr += message

print(messageStr.strip())

replaceStr = "I really like dogs"
newstr = replaceStr.replace("dog","cat")
print(newstr)