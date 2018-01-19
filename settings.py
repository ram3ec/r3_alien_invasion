class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200            # разрешение игрового поля
        self.screen_height = 800
        self.bg_color = (230, 230, 230)     # цвет фона

        # Настройки корабля
        self.ship_speed_factor = 1.5 #скорость корабля
        self.ship_limit = 3

        # Параметры пули
        self.bullet_speed_factor = 3 #скорость пули
        #self.bullet_width = 3
        self.bullet_width = self.screen_width / 10 # для тестирования-ширина пули
        self.bullet_height = 4 #толщина пули
        self.bullet_color = 60, 60, 60 #цвет
        self.bullets_allowed = 6
        self.bullet_inside = False

        # Настройки пришельцев
        self.alien_speed_factor = 2 # скорость пришельцев
        self.fleet_drop_speed = 10  #величина снижения флота при достижении края
        self.fleet_direction = 1    #1 - движение вправо, -1 - движение влево