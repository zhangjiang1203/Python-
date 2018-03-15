import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    """#初始化游戏并创建一个屏幕对象"""
    setting = Settings()

    pygame.init()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    """创建一艘飞船"""
    ship = Ship(setting,screen)
    bullets = Group()
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(setting,screen,ship,bullets)
        ship.update()#更新飞船的位置
        gf.update_bullets(bullets)
        gf.update_screen(setting,screen,ship,bullets)

run_game()