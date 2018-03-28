import csv
import matplotlib.pyplot as plt
from datetime import datetime
#获取天气数据并绘制图像
def get_temp_data():
    filename = "sitka_weather_2014.csv"
    try:
        with open(filename) as cv:
            reader = csv.reader(cv)
            header_row = next(reader)

            # 取出最高的天气温度
            highs, dates, lows = [], [], []
            # 由于我们已经读取了文件头行，这个循环将从第二行开始
            for row in reader:
                # 将数据信息转化成int类型在存储到数组中
                current = datetime.strptime(row[0], "%Y-%m-%d")
                dates.append(current)
                highs.append(row[1])
                lows.append(row[3])

            print(len(lows))
            # 绘制天气温度import matplotlib.pyplot as plt
            fig = plt.figure(dpi=128, figsize=(20, 12))
            plt.plot(dates, lows, c='blue')
            plt.plot(dates, highs, c='red')
            plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)

            plt.title("Daily high Temperatures,July 2014", fontsize=20)
            # 设置x轴显示文字为斜体格式
            fig.autofmt_xdate()
            plt.xlabel('', fontsize=14)
            plt.ylabel('Temperatures(F)', fontsize=14)
            plt.tick_params(axis='both', which='major', labelsize=14)
            plt.show()
    except FileNotFoundError:
        print("the file " + filename +" is not exit")


get_temp_data()