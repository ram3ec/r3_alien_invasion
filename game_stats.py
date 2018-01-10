class GameStats():
    """Отслеживание статистики для игры"""

    def __init__(self, ai_settings):
        """Инициализирует статистику"""
        self.ai_settings = ai_settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.ai_settings.ship_limit