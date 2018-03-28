from random import choice

class RandomWalk():
    def __init__(self,num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        #所有的随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        #不断漫步直到达到指定的长度
        while len(self.x_values) < self.num_points:
            #决定前进的方向以及沿这个方向前进的距离
            x_direction = choice([1,0])#一个选择值 向左或者向右
            x_distance = choice([0,1,2,3,4,5,6,7,8])
            x_step = x_direction *x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #不允许原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的位置
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            #添加到漫步数中
            self.x_values.append(next_x)
            self.y_values.append(next_y)