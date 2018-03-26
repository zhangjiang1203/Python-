import pygame.font
from ship import Ship
from pygame.sprite import Group

class Scoreboard():
    def __init__(self,setting,screen,status):
        self.screen = screen
        self.setting = setting
        self.status = status
        self.screen_rect = screen.get_rect()

        #设置显示积分的颜色和字体
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        self.draw_information()

    def draw_information(self):
        # 准备初始得分,等级，最高分和剩余飞船绘制
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_show_ship()

    def prep_score(self):
        """将得分转化为图片"""
        round_score = int(round(self.status.score,-1))
        score_str = "Score:" + "{:,}".format(round_score)
        self.score_image = self.font.render(score_str,True,self.text_color)

        #绘制分数
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = int(round(self.status.high_score,-1))
        high_str = "Highest Score:" + "{:,}".format(high_score)
        self.high_image = self.font.render(high_str,True,self.text_color)

       #绘制最高分
        self.high_rect = self.high_image.get_rect()
        self.high_rect.centerx = self.screen_rect.centerx
        self.high_rect.top = self.score_rect.top

    def prep_level(self):
        level_str = "level:" + str(self.status.level)
        self.level_image = self.font.render(level_str,True,self.text_color)

        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 10

    def prep_show_ship(self):
        self.ships = Group()
        for ship_num in range(self.status.ship_left):
            ship = Ship(self.setting,self.screen)
            ship.rect.x = 10 + ship_num * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_image,self.high_rect)
        self.screen.blit(self.level_image,self.level_image_rect)
        self.ships.draw(self.screen)