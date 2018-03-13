import pygame

class Ship():

    def __init__(self,setting,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.setting = setting

        """加载飞船图片并获取其外接矩形"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        """将每艘新飞船放在屏幕底部中央"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #飞船的center属性中存储小数
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # 添加一个移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        #限制飞船的活动范围
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.setting.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.centerx -= self.setting.ship_speed_factor
        elif self.moving_up and self.centery >= 24:
            self.centery -= self.setting.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.centery += self.setting.ship_speed_factor

        #更新self.center 更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery