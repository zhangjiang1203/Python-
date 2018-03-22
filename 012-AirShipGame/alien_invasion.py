import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_status import GameStatus
from button import Button
from scoreboard import Scoreboard

def run_game():
    """#初始化游戏并创建一个屏幕对象"""
    setting = Settings()
    pygame.init()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建一个用于存储游戏的统计信息的实例
    status = GameStatus(setting)
    sb = Scoreboard(setting,screen,status)
    """创建一艘飞船"""
    ship = Ship(setting,screen)
    bullets = Group()
    stars = Group()
    aliens = Group()
    gf.addGroupStars(setting, screen,stars)
    """创建外星人群"""
    gf.create_fleet(setting, screen, ship, aliens)
    #创建play按钮
    playBtn = Button(setting,screen,"play")
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(setting,screen,ship,status,aliens,bullets,playBtn)
        if status.game_active:
            ship.update()#更新飞船的位置
            gf.update_bullets(setting,screen,ship,aliens,bullets,status,sb)
            gf.update_aliens(setting,status,screen,ship,aliens,bullets)
        #刷新屏幕
        gf.update_screen(setting,screen,ship,aliens,bullets,stars,status,playBtn,sb)

run_game()