class Settings():
    """存储外星人的所有设置"""
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #设置飞船的移动速度
        self.ship_speed_factor = 3

        """设置子弹的速度 宽度 高度和颜色设置"""
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 8
        self.bullet_color = (60,60,60)