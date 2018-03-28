from random import randint

class Die():
    """表示一个骰子的类"""
    def __init__(self,number_size = 6):
        self.number_size = number_size

    #翻滚骰子
    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1,self.number_size)