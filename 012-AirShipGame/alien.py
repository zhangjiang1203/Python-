import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,setting,screen):
        """初始化外星人"""
        super(Alien,self).__init__()
        self.screen = screen
        self.setting = setting

        """加载外星人图像"""
        self.image = pygame.image.load('images/alien.png')#pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        """设置外星人的位置"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)