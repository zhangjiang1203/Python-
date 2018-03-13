import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """#初始化游戏并创建一个屏幕对象"""
    setting = Settings()

    pygame.init()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    """创建一艘飞船"""
    ship = Ship(setting,screen)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        #刷新屏幕
        gf.update_screen(setting,screen,ship)

run_game()