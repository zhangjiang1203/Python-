#coding=utf-8

import  os.path

filename = 'myname.txt'
if os.path.isfile(filename):
    f1 = open(filename,'r+')
else:
    f1 = open(filename,'w+')

while True:
    line = input('qing shu ru wen zi:')
    if line == "q" or line == "Q":
        break

    f1.write(line + '\n')

f1.close()