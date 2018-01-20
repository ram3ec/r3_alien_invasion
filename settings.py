class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1200                    # разрешение игрового поля
        self.screen_height = 800
        self.bg_color = (230, 230, 230)             # цвет фона

        # Настройки корабля
        self.ship_limit = 3                         # количество кораблей

        # Параметры пули
        self.bullet_width = self.screen_width / 10  # для тестирования-ширина пули
        self.bullet_height = 4                      # толщина пули
        self.bullet_color = 60, 60, 60              # цвет
        self.bullets_allowed = 6                    # пулей одновременно на экране
        self.bullet_inside = False                  # способность пули пролетать насквозь пришельца

        # Настройки пришельцев
        self.fleet_drop_speed = 10                  # величина снижения флота при достижении края

        # Настройка игры
        self.game_pause = 2                         # длительность паузы
        self.speedup_scale = 1.1                    # темп ускорения игры

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5                # скорость корабля
        self.bullet_speed_factor = 3                # скорость пули
        self.alien_speed_factor = 1                 # скорость пришельцев
        self.fleet_direction = 1                    # 1 - движение вправо, -1 - движение влево

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale