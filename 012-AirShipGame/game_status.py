import json
class GameStatus():
    def __init__(self,setting):
        self.setting = setting
        self.reset_status()
        #游戏刚开始的时候处于活动状态
        self.game_active = False
        # 最高得分
        self.high_score = 0
        self.get_high_score()

    def reset_status(self):
        self.ship_left = self.setting.ship_limit
        #游戏计分
        self.score = 0
        #游戏的等级
        self.level = 1

    #获取数据，打开文件，如果没有这个文件就创建一个初始化的值，添加到文件中
    def get_high_score(self):
        try:
            with open(self.setting.scorefile_name) as f_obj:
                score = json.load(f_obj)
        except FileNotFoundError:
            #文件不存在，创建一个文件并初始化数据
            with open(self.setting.scorefile_name,"w") as f_write:
                json.dump('0',f_write)
            msg = "Sorry, the file " + self.setting.scorefile_name + " does not exist."
            print(msg)
        else:
            print("拿到的数据"+score)
            self.high_score = int(score)