#coding=utf-8
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, first_settings, screen):  # 初始化飞船并设置其初始化位置
        super(Ship, self).__init__()
        self.first_settings = first_settings
        self.screen = screen  # 加载飞船图像并且获取其外接矩形
        self.image = pygame.image.load('images/iron_man.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 此下将每艘钢铁侠放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False


    def update(self):  # 根据移动标志调整钢铁侠的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.first_settings.ship_speed_factor  # 更新飞船的center值而不是rect值
        if self.moving_left and self.rect.left > 0:
            self.center -= self.first_settings.ship_speed_factor  # 更新飞船的center值而不是rect值
        self.rect.centerx = self.center  # 根据self.center更新rect对象


    def blitme(self):  # 在指定位置绘制钢铁侠
        self.screen.blit(self.image, self.rect)


    def center_ship(self):  # 让钢铁侠出现在屏幕中央
        self.center = self.screen_rect.centerx