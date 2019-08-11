#coding=utf-8
import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from thano import Thano
import game_functions as gf


# ------------------各种物件的速度 大小 灭霸 随机分布


def run_game():  # 初始化pygame、设置和屏幕对象
    pygame.init()
    first_settings = Settings()
    screen = pygame.display.set_mode((first_settings.screen_width, first_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(first_settings, screen, "Play")
    stats = GameStats(first_settings)  # 创建一个储存游戏统计信息的实例,并且创建记分牌
    sb = Scoreboard(first_settings, screen, stats)
    ship = Ship(first_settings, screen)  # 创建一架钢铁侠、一个子弹编组和一个泰坦飞船编组
    thano = Thano(first_settings, screen)
    bullets = Group()
    thanos = Group()
    gf.create_fleet(first_settings, screen, ship, thanos)
    # bg_color = (230,230,230) #设置背景颜色
    while True:  # 开始游戏的主循环
        gf.check_events(first_settings, screen, stats, sb, play_button, ship, thanos, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(first_settings, screen, stats, sb, ship, thanos, bullets)
            gf.update_thanos(first_settings, screen, stats, sb, ship, thanos, bullets)  # 传值对应顺序不能错
        gf.update_screen(first_settings, screen, stats, sb, ship, thanos, bullets, play_button)
        '''bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)
        #print(len(bullets))'''
        '''for event in pygame.event.get(): #监视键盘和鼠标事件
            if event.type == pygame.OUIT:
                    sys.exit()
        #screen.fill(bg_color) #每次循环重新绘制屏幕
        screen.fill(first_settings.bg_color)
        ship.blitme()
        pygame.display.flip() #让最近绘制的屏幕可见'''
run_game()

