import sys
import pygame
from bullet import Bullet
from star import Star

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
        if len(bullets) < setting.bullets_allow:
            new_bullet = Bullet(setting,screen,ship)
            bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()


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

def update_bullets(bullets):
    """更新子弹位置，并删除已经消失的子弹"""
    bullets.update()
    #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

"""刷新屏幕"""
def update_screen(ai_settings,screen,ship,alien,bullets,stars):
    screen.fill(ai_settings.bg_color)
    stars.draw(screen)  # 编组调用draw() 时，Pygame自动绘制编组的每个元素，绘制位置由元素的属性rect 决定
    #绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    #绘制飞船和外星人
    ship.blitme()
    alien.blitme()
    #最近绘制的屏幕可见
    pygame.display.flip()

def addGroupStars(setting,screen,stars):
    for number in range(1,100):
        myStar = Star(setting,screen)
        myStar.rect.x = myStar.getRandomPosition()
        myStar.rect.y = myStar.getRandomPosition()
        stars.add(myStar)
#
