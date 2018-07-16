
# __all__ = [a,b] 导入all列表中的元素 *不一定是引入所有的库
from tkinter import *
from tkinter import messagebox


def closeAllWindow():
    # 销毁窗口
    window.destroy()

# 定义关闭函数
def closeWindow():
    # 显示提示信息
    messagebox.showinfo(title='警告',message='我那么喜欢你，你不喜欢我，你真让我伤心啊，哈哈哈');
    # 显示错误信息
    # messagebox.showerror(title='错误信息',messagebox='你这是错误的，不要在点了，还是选择喜欢我吧，哈哈哈')

def dolike():
    # 顶级的窗口
    love = Toplevel(window)
    love.geometry('300x100+575+260')
    love.title('哈哈哈')
    showLabel = Label(love,text='好巧，我也喜欢你，我们在一起吧',font=('微软雅黑',18),fg='red')
    showLabel.pack()
    # 关闭所有的函数
    closeBtn = Button(love,text='好的啊',width=20,height=2,command=closeAllWindow)
    closeBtn.pack()

    love.protocol('WM_DELETE_WINDOW',dolove)


def dolove():
    return

def dounlike():
    no_love = Toplevel(window)
    no_love.geometry('300x200+575+260')
    no_love.title('不喜欢')

    showLabel = Label(no_love, text='在考虑一下呗，我们还是很合适的', font=('微软雅黑', 18), fg='red')
    showLabel.pack()
    # 关闭所有的函数
    closeBtn = Button(no_love, text='好的啊', width=20, height=2, command=no_love.destroy)
    closeBtn.pack() 
    no_love.protocol("WM_DELETE_WINDOW",noloveclose)

def noloveclose():
    # 不做任何操作
    # return
    # 点击关闭死循环
    dounlike()


window = Tk()
window.title('跟你表白了')
window.geometry('450x400+500+200')

# 添加label
infoLabel = Label(window,text='小姐姐，你好啊',font=('微软雅黑',18),fg='red',width=25)
infoLabel.grid(row=0,column=0,sticky=W)


#添加喜欢按钮
loveLabel = Label(window,text='喜欢我吗',font=('微软雅黑',30))
loveLabel.grid(row=1,column=1,sticky=W)

# 添加图片显示
loveImage = PhotoImage(file='lovepic.png')
loveImageLabel = Label(window,image=loveImage)
# 组件跨越的列数
loveImageLabel.grid(row=2,columnspan=2)

#添加按钮
likebtn = Button(window,text='喜欢',width=10,height=2,command=dolike)
likebtn.grid(row=3,column=0,sticky=W)

#添加按钮
unlikebtn = Button(window,text='不喜欢',width=10,height=2,command=dounlike)
unlikebtn.grid(row=3,column=1,sticky=E)


# 用户关闭窗口调用的事件
window.protocol("WM_DELETE_WINDOW",closeWindow)
# 消息循环
window.mainloop()