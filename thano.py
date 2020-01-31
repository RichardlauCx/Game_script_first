# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : Pycharm

import pygame
from pygame.sprite import Sprite


class Thano(Sprite):  # 表示单个泰坦飞船的类
    def __init__(self, first_settings, screen):  # 初始化泰坦并设置其起始位置
        super(Thano, self).__init__()
        self.screen = screen
        self.first_settings = first_settings

        self.image = pygame.image.load('images/Thanos_dirigible.jpg')
        self.rect = self.image.get_rect()  # 加载泰坦飞船图像并设置其rect属性

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height  # 每个泰坦飞船图像最初都在屏幕左上角附近

        self.x = float(self.rect.x)  # 存储泰坦飞船的准确位置

    def blitme(self):  # 在指定位置绘制泰坦飞船
        self.screen.blit(self.image, self.rect)

    def update(self):  # 向右移动泰坦飞船
        self.x += (self.first_settings.thano_speed_factor * self.first_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()  # 若位于边缘就返回True
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True