class Settings():
    """存储外星人的所有设置"""
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)
        #显示飞船数量
        self.ship_limit = 3

        """设置子弹的速度 宽度 高度和颜色设置"""
        self.bullet_width = 3
        self.bullet_height = 8
        self.bullet_color = (255,255,255)
        # 限制子弹的个数
        self.bullets_allow = 1000

        """设置显示星星的数量"""
        self.star_number = 100
        """外星人移动的速度"""
        self.fleet_drop_speed = 10
        # 每次消灭完了外星人就开始加速
        self.speedup_scale = 2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # 设置飞船的移动速度
        self.ship_speed_factor = 1.5
        # 设置子弹的移动速度
        self.bullet_speed_factor = 3
        # 外星人移动的速度
        self.alien_speed_factor = 1
        # 外星人移动的方向 1 向右 -1 向左
        self.fleet_direction = 1
        # 每次击落之后添加的分数
        self.alien_point = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        #提高分数
        self.alien_point = int(self.alien_point * self.speedup_scale)