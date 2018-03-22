class GameStatus():
    def __init__(self,setting):
        self.setting = setting
        self.reset_status()
        #游戏刚开始的时候处于活动状态
        self.game_active = False

    def reset_status(self):
        self.ship_left = self.setting.ship_limit
        #游戏计分
        self.score = 0
