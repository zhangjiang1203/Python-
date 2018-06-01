
import os
import os.path
#
# try:
#     with open('name.txt','w+') as fileObject:
#         content = fileObject.read()
#         # 写入到文件中去显示
#         for line in (i ** 2 for i in range(1, 11)):
#             fileObject.write(str(line) + '\n')
#
# except FileNotFoundError:
#     print("文件没有发现")
# else:
#     #获取到的文件类容
#     print(content)

  # '''
  # 目录文件操作 os模块的常用方法
  #   1.chdir()：改变工作目录
  #   2.chroot():设定当前进程的根目录
  #   3.listdir():列出指定目录下的所有文件名
  #   4.mkdir() 创建指定目录
  #   5.makedirs() 创建多级目录
  #   6.getcwd() 获取当前目录路径
  #   7.rmdir() 移除当前目录
  #   8.removedirs() 移除多级目录
  # 文件
  #   1.mkfifo() 创建文件
  #   2.mknod() 创建设备文件
  #
  # '''

filename = 'test.txt'
if os.path.isfile(filename):
    f1 = open(filename,'w+')
else:
    f1 = open(filename,'a+')

while True:
    line = input('Enter something')
    if line == 'q' or line == 'quit':
       break
    f1.write(line + '\n')

f1.close()




