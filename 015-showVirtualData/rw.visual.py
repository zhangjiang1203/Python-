import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:

    #创建一个实例
    rw = RandomWalk(50000)
    rw.fill_walk()
    plt.figure(figsize=(10, 6))

    point_num = list(range(rw.num_points))
    #绘制随机点
    plt.scatter(rw.x_values,rw.y_values,c=point_num,cmap=plt.cm.Reds,edgecolors='none',s=1)
    #绘制线条
    # plt.plot(rw.x_values,rw.y_values,linewidth=1)
    plt.title("random walk number")
    plt.xlabel("number",fontsize=14)
    plt.ylabel("walk",fontsize=14)

    #突出起点和终点
    # plt.scatter(0,0,c='green',edgecolors='none',s=15)
    # plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=15)

    #隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keeping_run = input("make another walk?(y/n)")
    if keeping_run == 'n':
        break