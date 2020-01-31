# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : Pycharm


class Settings():  # 存储外星人入侵项目所有设置的类
    def __init__(self):  # 初始化游戏的设置
        """初始化游戏的静态设置"""
        self.screen_width = 1500  # 对屏幕的设置
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_limit = 3  # 飞船数量

        self.bullet_width = 6    # 9
        self.bullet_width = 6    # 6
        self.bullet_height = 15
        self.bullet_color = 99, 99, 99
        self.bullets_allowed = 6

        self.fleet_drop_speed = 6
        self.speedup_scale = 1.1  # 以什么样的速度来加快游戏节奏
        self.score_scale = 1.5  # 外星人点数提高的速度
        # available_space_x = first_settings.screen_width - (2 * thanos_width)
        # number_thanos_x = available_space_x / (2 * thanos_width)

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):  # 初始化随着游戏进行的变化设置
        self.ship_speed_factor = 9 #1.5
        self.bullet_speed_factor = 8 #3
        self.thano_speed_factor = 2 #2  # 泰坦飞船设置
        self.fleet_direction = 1  # 为1时表示向右移动，为-1时表示向左移动
        self.thano_points = 50

    def increase_speed(self):  # 提高速度设置还有外星人点数
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.thano_speed_factor *= self.speedup_scale
        self.thano_points = int(self.thano_points * self.score_scale)
        # print(self.thano_points)