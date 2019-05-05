#coding=utf-8
class GameStats():  # 跟踪游戏的统计信息
    def __init__(self, first_settings):  # 初始化统计信息
        self.first_settings = first_settings
        self.reset_stats()
        self.game_active = False  # 让游戏一开始处于非活动状态
        self.high_score = 0

    def reset_stats(self):  # 初始化在游戏运行期间可能会变化的统计信息
        self.ships_left = self.first_settings.ship_limit
        self.score = 0
        self.level = 1