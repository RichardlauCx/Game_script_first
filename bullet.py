#coding=utf-8
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # 对飞船发射的子弹进行管理的类
    def __init__(self, first_settings, screen, ship):  # 在飞船所处的位置创建一个子弹对象
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, first_settings.bullet_width,first_settings.bullet_height)  # 在0,0处创建一个表示子弹的矩形，再设置正确的位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)  # 储存用小数表示子弹的位置
        self.color = first_settings.bullet_color
        self.speed_factor = first_settings.bullet_speed_factor

    def update(self):  # 向上移动子弹
        self.y -= self.speed_factor  # 更新并表示子弹位置的小数值
        self.rect.y = self.y  # 更新子弹的rect的位置

    def draw_bullet(self):  # 屏幕上面绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
