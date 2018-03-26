import sys
import pygame
from bullet import Bullet
from star import Star
from alien import Alien
from time import sleep
import json

def check_keydown_events(event,setting,screen,ship,bullets,status):
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
        save_high_score(setting, status)


def check_keyup_events(event,ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(setting,screen,ship,status,aliens,bullets,playBtn,sb):
    """响应鼠标和按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_high_score(setting,status)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,setting,screen,ship,bullets,status)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(setting,screen,ship,status,playBtn,mouse_x,mouse_y,aliens,bullets,sb)

#系统退出之前存储最高得分
def save_high_score(setting,status):
    filename = setting.scorefile_name
    with open(filename, "w") as file_object:
        myMessage = str(status.score) #file_object.read()
        json.dump(myMessage,file_object)
        # file_object.write(myMessage)
        sys.exit()



def check_play_button(setting,screen,ship,status,playBtn,mouse_x,mouse_y,aliens,bullets,sb):
    """玩家点击play按钮的时候开始新游戏"""
    button_click = playBtn.rect.collidepoint(mouse_x,mouse_y)
    #按钮消失了 可是点击按钮之前的区域还是会重置游戏，加上只在游戏game_active为False状态下可以点击
    if button_click and not status.game_active:
        #重置游戏参数
        setting.initialize_dynamic_settings()
        #开始的时候隐藏光标
        pygame.mouse.set_visible(False)
        status.reset_status()
        status.game_active = True

        #重置记分牌,等级，剩余飞船数 最高分
        sb.draw_information()

        # 清空子弹和外星人
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，飞船放到屏幕底端中央
        create_fleet(setting, screen, ship, aliens)
        ship.center_ship()


def update_bullets(setting,screen,ship,aliens,bullets,status,sb):
    """更新子弹位置，并删除已经消失的子弹"""
    bullets.update()
    #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(setting,screen,ship,aliens,bullets,status,sb)

def check_bullet_alien_collisions(setting,screen,ship,aliens,bullets,status,sb):
    # 检查是否有子弹击中了外星人
    # 如果是这样就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    """如果在一次循环中有两颗子弹射中了外星人，
       或者因子弹更宽而同时击中了多个外星人，
       玩家将只能得到一个被消灭 的外星人的点数,修改检测子弹和外星人碰撞的方式
    """
    #与外星人碰撞的子弹都是字典collisions中的一个键;
    #而与每颗子弹相关的值都是一个列表，其中包含该子弹撞到的外星人。
    # 我们遍历字典collisions ，确保将消灭的每个外星人的点数都记入得分:
    if collisions:#如果有子弹和外星人碰撞就添加分数
        for aliens in collisions.values():
            status.score += setting.alien_point * len(aliens)
            #重新绘制
            sb.prep_score()
        check_high_score(status,sb)#刷新最高分

    # 删除所有的子弹  #外星人都全部移除之后创建新的一群外星人
    if len(aliens) == 0:
        bullets.empty()
        setting.increase_speed()
        # 整群外星人都消失 增加一个等级 刷新等级显示
        status.level += 1
        sb.prep_level()
        create_fleet(setting, screen, ship, aliens)

"""刷新屏幕"""
def update_screen(ai_settings,screen,ship,aliens,bullets,stars,status,playBtn,sb):
    screen.fill(ai_settings.bg_color)
    # 编组调用draw() 时，Pygame自动绘制编组的每个元素，绘制位置由元素的属性rect决定
    stars.draw(screen)
    #绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    #绘制飞船和外星人
    ship.blitme()
    #绘制外星人群
    aliens.draw(screen)
    sb.show_score() #显示分数、等级和剩余飞船
    #最近绘制的屏幕可见
    if not status.game_active:
        playBtn.draw_button()
    pygame.display.flip()

def addGroupStars(setting,screen,stars):
    for number in range(1,setting.star_number):
        myStar = Star(setting,screen)
        myStar.rect.x = myStar.getRandomPosition()
        myStar.rect.y = myStar.getRandomPosition()
        stars.add(myStar)

def get_number_aliens_x(setting,alien_width):
    """计算一行可以放下几个外星人"""
    available_space_x = setting.screen_width - 2 * alien_width
    number_alien = int(available_space_x / (2 * alien_width))
    return number_alien

def get_number_rows(setting,ship_height,alien_height):
    """计算可以容纳多少行外星人"""
    #屏幕的高度-外星人的上边距(外星人高度)-飞船的高度-最初飞船和外星人的距离(外星人高度的两倍)
    #每行外星人之间有一个外星人高度的空间
    available_space_y = setting.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(setting,screen,aliens,alien_number,row_number):
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(setting,screen,ship,aliens):
    """创建外星人群"""
    alien = Alien(setting,screen)
    """计算一行可以放下几个外星人"""
    alien_number_x = get_number_aliens_x(setting,alien.rect.width)
    number_rows = get_number_rows(setting,ship.rect.height,alien.rect.height)
    for row in range(number_rows):
        for alien_number in range(alien_number_x):
            create_alien(setting,screen,aliens,alien_number,row)


def check_fleet_edges(setting,aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(setting,aliens)
            break

def change_fleet_direction(setting,aliens):
    """将整群外星人下移"""
    for alien in aliens:
        alien.rect.y += setting.fleet_drop_speed
    setting.fleet_direction *= -1

def update_aliens(setting,status,screen,ship,aliens,bullets,sb):
    #遍历删除底部超出边界的外星人
    # for aline in aliens.copy():
    #     if aline.rect.y >= (setting.screen_height-aline.rect.height):
    #         aliens.remove(aline)
    #检查是否有外星人位于边界，并更新外星人的位置
    check_fleet_edges(setting,aliens)
    #更新外星人的所有位置信息
    #对编组aliens 调用方法update() ，这将自动对每个外星人调用方法update()
    aliens.update()
    #检测是否有外星人到达屏幕底端
    check_aliens_bottom(setting,screen,ship,aliens,bullets,status,sb)

    #检测外星人和飞船之间的碰撞,一个精灵和一个编组。它检查编组是否有成员与精灵发生了碰撞,没有碰撞返回None
    if pygame.sprite.spritecollideany(ship,aliens):
        #重新绘制飞船和外星人
        print("开始碰撞了")
        ship_hit(setting,screen,ship,aliens,bullets,status,sb)


def ship_hit(setting,screen,ship,aliens,bullets,status,sb):
    """相应被撞到的飞船"""
    if status.ship_left > 0:
        status.ship_left -= 1
        #清空子弹和外星人
        aliens.empty()
        bullets.empty()
        #刷新剩余飞船数
        sb.prep_show_ship()

        #创建一群新的外星人，飞船放到屏幕底端中央
        create_fleet(setting,screen,ship,aliens)
        ship.center_ship()
        #暂停
        sleep(0.5)
    else:
        status.game_active = False
        #游戏结束了显示光标
        pygame.mouse.set_visible(True)

def check_aliens_bottom(setting,screen,ship,aliens,bullets,status,sb):
    """检测是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            """飞船被撞到一样处理事件"""
            ship_hit(setting,screen,ship,aliens,bullets,status,sb)
            break

def check_high_score(status,sb):
    if status.score > status.high_score:
        status.high_score = status.score
        sb.prep_high_score()