# 引入python GUI类库创建界面
from tkinter import *
import requests
# 解析html
from bs4 import BeautifulSoup

header = {
             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }

# 爬取网页数据
def download_song():
    # 获取用户输入的URL地址
    #  url = entry.get()
    # 下载的url https://music.163.com/#/playlist?id=2302000737
    url = "https://music.163.com/playlist?id=2302000737"
    song_url = "http://music.163.com/song/media/outer/url?id={}"
    result = requests.get(url,headers=header)
    html = BeautifulSoup(result.text,'html.parser')
    print(html)
    musics = html.find('ul',{'class','f-hide'}).find_all('a')
    music_dict = {}
    for music in musics[0:1]:
        music_id = music.get('href').strip('/song?id=')
        music_name = music.text
        music_dict[music_id] = music_name


    # 拿到下载路径和文件保存路径
    for k,v in music_dict.items():
        download_url = song_url.format(k)
        save_path = '/Users/zitang/Download/musics/%s.mp3' %v
        #开始下载数据
        result = requests.get(download_url,headers=header)
        with open(save_path,'wb') as w_obj:
            w_obj.write(result)



download_song()


# 创建窗口
root = Tk()
# 设置标题
root.title('网易云音乐')
# 设置窗口大小,x 区分宽高
# root.geometry('500x400')
# 设置出现的位置,用+号来代替，这个是相对屏幕左上角的位置
# root.geometry('+500+200')
# 两句合成一句是执行
root.geometry('560x300+500+200')

# 标签控件
label = Label(root,text='请输入要下载的歌单URL:',font=('华文行楷',12))
# 添加定位才能显示
# 网格式布局 以行列为准显示
label.grid(row=0,column=0)

# 输入框
entry = Entry(root,font=('微软雅黑',25),width=25)
entry.grid(row=0,column=1)

text = Listbox(root,font=('微软雅黑',15),width=55,height=10)
# 组件跨越的列数
text.grid(row=1,columnspan=2)


# 添加下载按钮和退出按钮
download = Button(root,text='开始下载',font=('微软雅黑',15),width=10,height=2)
# 添加最后的对齐方式
# sticky对齐方式 N S W E
download.grid(row=2,column=0,sticky=W)

exit = Button(root,text='退出',font=('微软雅黑',15),width=10,height=2,command=root.quit())
# 添加最后的对齐方式
# sticky对齐方式 N S W E
exit.grid(row=2,column=1,sticky=E)

# 显示窗口,消息循环
root.mainloop()

