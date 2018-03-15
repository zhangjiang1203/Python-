import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,setting,screen,ship,bullets):
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(setting,screen,ship)
        bullets.add(new_bullet)


def check_keyup_events(event,ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(setting,screen,ship,bullets):
    """响应鼠标和按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,setting,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


"""刷新屏幕"""
def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)
    #绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    #最近绘制的屏幕可见
    pygame.display.flip()