import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from star import Star

def run_game():
    """#初始化游戏并创建一个屏幕对象"""
    setting = Settings()

    pygame.init()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    """创建一艘飞船"""
    ship = Ship(setting,screen)
    """创建一个外星人"""
    alien = Alien(setting,screen)
    bullets = Group()
    stars = Group()
    gf.addGroupStars(setting, screen,stars)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(setting,screen,ship,bullets)
        ship.update()#更新飞船的位置
        gf.update_bullets(bullets)
        #刷新屏幕
        gf.update_screen(setting,screen,ship,alien,bullets,stars)

run_game()