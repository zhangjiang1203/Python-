import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    def __init__(self,setting,screen):
        super(Star,self).__init__()

        self.setting = setting
        self.screen = screen
        #获取图片
        self.image = pygame.image.load("images/star.png")
        self.rect = self.image.get_rect()

        # self.random_number = randint(10, 100)
        #设置星星的位置
        self.rect.x = 200
        self.rect.y = 300

    def getRandomPosition(self):
        return randint(50,1200)

    def blitme(self):
        self.screen.blit(self.image,self.rect)



