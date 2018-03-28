from die import Die
import matplotlib.pyplot as plt
import pygal
#ADD:同时掷两枚骰子

die1 = Die()
die2 = Die(8)

#掷骰子 将结果存储起来
results = []
for roll_num in range(10000):
     result = die1.roll() + die2.roll()
     results.append(result)

#分析每个数据出现的次数
frequencies = []
maxValue = range(2,die1.number_size+die2.number_size+1)
for value in maxValue:
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

#绘制直方图
hist = pygal.Bar()
hist.title = "绘制骰子的出现次数"
hist.x_labels = list(maxValue)
hist._x_title = "Result"
hist._y_title = "Frequency of result"
hist.add("D6+D6",frequencies)
hist.add("custom",[200,300,500,1000,1240,110,1190,1100,1008,1220,987])
#存储为一个svg文件 文件格式必须是svg
hist.render_to_file('die_visual1.svg')


plt.title("Frequency")
plt.xlabel("value",fontsize=14)
plt.ylabel("frequency",fontsize=14)
#绘制点
# plt.scatter(list(maxValue),frequencies,c=frequencies,cmap=plt.cm.Reds,s=10,edgecolors='none')
#绘制线 c=修改显示的颜色
plt.plot(list(maxValue),frequencies,c=(0.7,0.1,0.8),linewidth=1)
plt.show()