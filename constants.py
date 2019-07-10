import pygame

pygame.init()

# Размер окна
game_width = 800
game_height = 600
cell_width = 32
cell_height = 32


# Что то связанное с картой
map_width = 32
map_height = 32

# Назначение цветов
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_grey = (100, 100, 100)

# Цвета игры
color_default_bg = color_grey

# Спрайты
s_player = pygame.image.load("data/s_player.png")
s_enemy = pygame.image.load("data/s_enemy1.png")
s_wall = pygame.image.load("data/s_wall.jpg")
s_floor = pygame.image.load("data/s_floor.jpg")
