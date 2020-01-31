# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : Pycharm

import sys
from time import sleep
import pygame
from bullet import Bullet
from thano import Thano


def check_keydown_events(event, first_settings, screen, ship, bullets):  # 响应按键
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:  # 向右移动钢铁侠
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:  # 创建一颗子弹并且将其加入到编组bullets中
            fire_bullet(first_settings, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()
            '''if len(bullets) < first_settings.bullets_allowed:
                new_bullet = Bullet(first_settings,screen,ship)
           
                bullets.add(new_bullet)'''


def fire_bullet(first_settings, screen, ship, bullets):  # 如果未达到极限就发射一个子弹
    if len(bullets) < first_settings.bullets_allowed:  # 创建新子弹、并将其加入到编组bullets中
        new_bullet = Bullet(first_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):  # 响应松开
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def check_events(first_settings, screen, stats, sb, play_button, ship, thanos, bullets):  # 相应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, first_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(first_settings, screen, stats, sb, play_button, ship, thanos, bullets, mouse_x, mouse_y)


def check_play_button(first_settings, screen, stats, sb, play_button, ship, thanos, bullets, mouse_x, mouse_y):  # 在玩家点击Play按钮时，开始游戏
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        button_cliked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_cliked and not stats.game_active:
            first_settings.initialize_dynamic_settings()  # 重置游戏设置
            pygame.mouse.set_visible(False)  # 隐藏光标
            stats.reset_stats()  # 重置游戏统计信息
            stats.game_active = True
            thanos.empty()
            bullets.empty()

            sb.prep_score()  # 重置记分牌图像
            sb.prep_high_score()
            sb.prep_level()
            sb.prep_ships()

            create_fleet(first_settings, screen, ship, thanos)  # 创建一群新的灭霸飞船，并将其居中
            ship.center_ship()


def update_screen(first_settings, screen, stats, sb, ship, thanos, bullets, play_button):  # 更新屏幕什么的图像，同时切换到新的屏幕
    screen.fill(first_settings.bg_color)  # 每次循环都重新绘制屏幕
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    thanos.draw(screen)
    # thano.blitme()
    sb.show_score()
    if not stats.game_active:  # 如果为非活动状态，就绘制Play按钮
        play_button.draw_button()
    pygame.display.flip()  # 让最近绘制的屏幕可见


def update_bullets(first_settings, screen, stats, sb, ship, thanos, bullets):  # 更新子弹的位置，并且删除已经消失的子弹
    bullets.update()  # 更新子弹的位置
    for bullet in bullets.copy():  # 删除已经消失的子弹
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullets_thano_collisions(first_settings, screen, stats, sb, ship, thanos, bullets)


def check_bullets_thano_collisions(first_settings, screen, stats, sb, ship, thanos, bullets):
    collisions = pygame.sprite.groupcollide(bullets, thanos, True, True)
    if collisions:
        for thanos in collisions.values():
            stats.score += first_settings.thano_points * len(thanos)
            sb.prep_score()
        check_high_score(stats, sb)
    if(len(thanos)) == 0:  # 删除现有子弹,加快速度，并且重新创建一波灭霸飞船,同时提升一个等级
        bullets.empty()
        first_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(first_settings, screen, ship, thanos)


def update_thanos(first_settings, screen, stats,sb, ship, thanos, bullets):  # 更新所有外星人的位置
    check_fleet_edges(first_settings, thanos)
    thanos.update()
    if pygame.sprite.spritecollideany(ship, thanos):
        ship_hit(first_settings, screen, stats, sb, ship, thanos, bullets)
        print("Iron man crashes!")
    check_thanos_bottom(first_settings, screen, stats, sb, ship, thanos, bullets)  # 检查灭霸是否到达


def create_fleet(first_settings, screen, ship, thanos):  # 创建外星人群
    thano = Thano(first_settings, screen)
    number_thanos_x = get_number_thanos_x(first_settings, thano.rect.width)     # ---------------检查此函数的bug
    number_rows = get_number_rows(first_settings, ship.rect.height, thano.rect.height)
    for row_number in range(number_rows):
        for thano_number in range(number_thanos_x):
            create_thano(first_settings, screen, thanos, thano_number, row_number)


def get_number_thanos_x(first_settings, thano_width):  # 计算每行可以容纳多少泰坦飞船，间距为泰坦飞船宽度
    available_space_x = first_settings.screen_width - 2 * thano_width
    number_thanos_x = int(available_space_x / (2 * thano_width))
    return number_thanos_x


def create_thano(first_settings, screen, thanos, thano_number, row_number):  # 创建一个泰坦飞船并且将其加入当前行
    thano = Thano(first_settings, screen)
    thano_width = thano.rect.width
    thano.x = thano_width + 2 * thano_width * thano_number
    thano.rect.x = thano.x
    thano.rect.y = thano.rect.height + 2 * thano.rect.height * row_number
    thanos.add(thano)


def get_number_rows(first_settings, ship_height, thano_height):
    available_space_y = (first_settings.screen_height - (3 * thano_height - ship_height))
    number_rows = int(available_space_y / (2 * thano_height))
    return number_rows


def check_fleet_edges(first_settings, thanos):  # 外星人到达边缘以后采取的措施
    for thano in thanos.sprites():
        if thano.check_edges():
            change_fleet_direction(first_settings, thanos)
            break


def change_fleet_direction(first_settings, thanos):
    for thano in thanos.sprites():
        thano.rect.y += first_settings.fleet_drop_speed  # 将整群泰坦飞船向下移，并且改变它们移动的方向
    first_settings.fleet_direction *= -1


def ship_hit(first_setting, screen, stats, sb, ship, thanos, bullets):  # 相应被外星人撞击的钢铁侠
    if stats.ships_left > 0:
        stats.ships_left -= 1  # 将数值减一
        sb.prep_ships()  # 更新记分牌
        thanos.empty()  # 清空灭霸飞船和发射的激光炮
        bullets.empty()
        create_fleet(first_setting, screen, ship, thanos)
        ship.center_ship()
        sleep(0.5)  # 暂停0.5秒
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_thanos_bottom(first_settings, screen, stats, sb, ship, thanos, bullets):  # 检查灭霸飞船是否已经登陆我方
    screen_rect = screen.get_rect()
    for thano in thanos.sprites():
        if thano.rect.bottom >= screen_rect.bottom:  # 碰撞处理
            ship_hit(first_settings, screen, stats, sb, ship, thanos, bullets)
            break


def check_high_score(stats, sb):  # 检查是否诞生了新的最高分
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()