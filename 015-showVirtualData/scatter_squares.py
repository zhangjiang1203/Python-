import matplotlib.pyplot as plt
#绘制一个点 s 表示绘制的时候点大小的尺寸
#plt.scatter(1,2,s=200)
#绘制一系列点(x,y,)
# plt.scatter([1,2,3,4,5],[1,8,27,64,125],s=100)
x_values = list(range(1,1001))
y_values = [x**3 for x in x_values]
#删除数据点的轮廓 设置edgecolor为none 默认为蓝色点和黑色轮廓
# plt.scatter(x_values,y_values,edgecolor='none',s=40)
#自定义颜色 设置参数c，将其设置为要设置的颜色
# plt.scatter(x_values,y_values,c=(0.1,0.9,0.5),edgecolor='none',s=40,linewidths=[1,4])
#设置绘制数据的颜色映射设置cmap
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,edgecolors='none',s=40)
plt.title("Square number")
plt.xlabel("value",fontsize=14)
plt.ylabel("square of number",fontsize=14)
#设置标尺
plt.tick_params(axis="both",which='major',labelsize=14)

#设置每个坐标轴的取值范围
# plt.axis([0,1100,0,1100000])
#把show替换为savefig，保存图片到本地文件所在的文件夹，bbox_inches为将多余的空白区域裁剪掉
#plt.savefig('myTable.png',bbox_inches='tight')
plt.show()