import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
input_value= [1,2,3,4,5]
# 参数说明
#参数说明  (x坐标值,y坐标值,线条的宽度)
plt.plot(input_value,squares,linewidth=5)
#设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#标记刻度的大小
plt.tick_params(axis='both',labelsize=14)
#打开matplotlib查看器，并显示绘制的图形
plt.show()