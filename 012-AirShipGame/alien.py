import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,setting,screen):
        """初始化外星人"""
        super(Alien,self).__init__()
        self.screen = screen
        self.setting = setting

        """加载外星人图像"""
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        """设置外星人的位置"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)


    def blitme(self):
        """指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """如果外星人处于屏幕边缘就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.setting.alien_speed_factor * self.setting.fleet_direction)
        self.rect.x = self.x