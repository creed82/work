import pygame
import constants

import tcod as libtcod


#      _______..___________..______       __    __    ______ .___________.
#     /       ||           ||   _  \     |  |  |  |  /      ||           |
#    |   (----``---|  |----`|  |_)  |    |  |  |  | |  ,----'`---|  |----`
#     \   \        |  |     |      /     |  |  |  | |  |         |  |
# .----)   |       |  |     |  |\  \----.|  `--'  | |  `----.    |  |
# |_______/        |__|     | _| `._____| \______/   \______|    |__|

class struct_Tile:
    def __init__(self, block_path):
        self.block_path = block_path


#   ___    ____        _   _____    ____   _____   ____
#  / _ \  | __ )      | | | ____|  / ___| |_   _| / ___|
# | | | | |  _ \   _  | | |  _|   | |       | |   \___ \
# | |_| | | |_) | | |_| | | |___  | |___    | |    ___) |
#  \___/  |____/   \___/  |_____|  \____|   |_|   |____/


class obj_Actor:

    def __init__(self, x, y, name_object, sprite, creature=None, ai=None):
        self.x = x  # map address
        self.y = y  # map address
        self.sprite = sprite
        self.creature = creature
        if creature:
            creature.owner = self
        self.ai = ai
        if ai:
            ai.owner = self

    def draw(self):
        SURFACE_MAIN.blit(self.sprite, (self.x * constants.cell_width, self.y * constants.cell_height))


#   ____    ___    __  __   ____     ___    _   _   _____   _   _   _____   ____
#  / ___|  / _ \  |  \/  | |  _ \   / _ \  | \ | | | ____| | \ | | |_   _| / ___|
# | |     | | | | | |\/| | | |_) | | | | | |  \| | |  _|   |  \| |   | |   \___ \
# | |___  | |_| | | |  | | |  __/  | |_| | | |\  | | |___  | |\  |   | |    ___) |
#  \____|  \___/  |_|  |_| |_|      \___/  |_| \_| |_____| |_| \_|   |_|   |____/

class com_Creature:
    """
    Существа имеют уровень жизни, и могут наносить урон объектам которые их атакуют. Существа могут умирать.
    """

    def __init__(self, name_instance, hp=10, death_function=None):
        self.name_instance = name_instance
        self.maxhp = hp
        self.hp = hp
        self.death_function = death_function

    def move(self, dx, dy):

        tile_is_wall = (GAME_MAP[self.owner.x + dx][self.owner.y + dy].block_path == True)

        target = map_check_for_creatures(self.owner.x + dx, self.owner.y + dy, self.owner)

        if target:
            self.attack(target, 5)

        if not tile_is_wall and target is None:

            self.owner.x += dx
            self.owner.y += dy

    def attack(self, target, damage):
        print(self.name_instance + ' attacks ' + target.creature.name_instance + ' for ' + str(damage) + ' damage!')
        target.creature.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        print(self.name_instance + "'s health is " + str(self.hp) + '/' + str(self.maxhp))

        if self.hp <= 0:

            if self.death_function is not None:
                self.death_function(self.owner)


# class com_Item:

# class com_Container:


#     _      ___
#    / \    |_ _|
#   / _ \    | |
#  / ___ \   | |
# /_/   \_\ |___|


class ai_Test:
    """Выполнение за ход"""

    def take_turn(self):
        self.owner.creature.move(libtcod.random_get_int(0, -1, 1), libtcod.random_get_int(0, -1, 1))


def death_monster(monster):
    """On death, most monsters stop moving"""
    print(monster.creature.name_instance + ' is dead!')

    monster.creature = None
    monster.ai = None


#  __  __      _      ____
# |  \/  |    / \    |  _ \
# | |\/| |   / _ \   | |_) |
# | |  | |  / ___ \  |  __/
# |_|  |_| /_/   \_\ |_|


def map_create():
    new_map = [[struct_Tile(False) for y in range(0, constants.map_height)] for x in range(0, constants.map_width)]

    new_map[10][10].block_path = True
    new_map[10][15].block_path = True

    for x in range(constants.map_width):
        new_map[x][0].block_path = True
        new_map[x][constants.map_height - 1].block_path = True

    for y in range(constants.map_height):
        new_map[0][y].block_path = True
        new_map[constants.map_width - 1][y].block_path = True

    return new_map


def map_check_for_creatures(x, y, exclude_object=None):
    target = None

    if exclude_object:

        for object in GAME_OBJECTS:
            if (object is not exclude_object and
                    object.x == x and
                    object.y == y and
                    object.creature):

                target = object

            if target:
                return target


    else:

        for object in GAME_OBJECTS:
            if (object.x == x and
                    object.y == y and
                    object.creature):

                target = object

            if target:
                return target


def map_make_fov(incoming_map):
    global FOV_MAP

    FOV_MAP = libtcod.map_new(constants.map_width,constants.map_height)

    for y in range(constants.map_height):
        for x in range(constants.map_width):
            libtcod.map_set_properties(FOV_MAP,x,y,
                                       not incoming_map[x][y].block_path,
                                       not incoming_map[x][y].block_path)

def map_calculate_fov():
    global FOV_CALCULATE

    if FOV_CALCULATE:
        FOV_CALCULATE = False
        libtcod.map_compute_fov(FOV_MAP,PLAYER.x, PLAYER.y, constants.TORCH_RADIUS,
                                constants.FOV_LIGHT_WALLS,constants.FOV_ALGO)


#  ____    ____       _     __        __  ___   _   _    ____
# |  _ \  |  _ \     / \    \ \      / / |_ _| | \ | |  / ___|
# | | | | | |_) |   / _ \    \ \ /\ / /   | |  |  \| | | |  _
# | |_| | |  _ <   / ___ \    \ V  V /    | |  | |\  | | |_| |
# |____/  |_| \_\ /_/   \_\    \_/\_/    |___| |_| \_|  \____|

def draw_game():
    global SURFACE_MAIN

    # Очистить экран
    SURFACE_MAIN.fill(constants.color_default_bg)

    # Нарисовать карту
    draw_map(GAME_MAP)

    # Нарисовать вес объекты
    for obj in GAME_OBJECTS:
        obj.draw()
    # Обновить экран
    pygame.display.flip()


def draw_map(map_to_draw):
    for x in range(0, constants.map_width):
        for y in range(0, constants.map_height):
            if map_to_draw[x][y].block_path == True:
                SURFACE_MAIN.blit(constants.s_wall, (x * constants.cell_width, y * constants.map_height))
            else:
                # рисуем пол
                SURFACE_MAIN.blit(constants.s_floor, (x * constants.cell_width, y * constants.map_height))


#   ____      _      __  __   _____
#  / ___|    / \    |  \/  | | ____|
# | |  _    / _ \   | |\/| | |  _|
# | |_| |  / ___ \  | |  | | | |___
#  \____| /_/   \_\ |_|  |_| |_____|

def game_main_loop():
    """Запускаем главный цикл игры"""

    game_quit = False

    # Определение действий игрока
    player_action = 'no-action'

    while not game_quit:

        # Пользовательский ввод
        player_action = game_handle_keys()
        if player_action == 'QUIT':
            game_quit = True

        elif player_action != 'no-action':
            for obj in GAME_OBJECTS:
                if obj.ai:
                    obj.ai.take_turn()

        # рисуем в главном цикле
        draw_game()

    # выход из игры
    pygame.quit()
    exit()


def game_initialization():
    """Инициализируем главное окно и pygame"""

    global SURFACE_MAIN, GAME_MAP, PLAYER, ENEMY, GAME_OBJECTS, FOV_CALCULATE

    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode((constants.map_width * constants.cell_width,
                                            constants.map_height * constants.cell_height))

    GAME_MAP = map_create()

    FOV_CALCULATE = True

    creature_com1 = com_Creature('Greg')
    PLAYER = obj_Actor(1, 1, 'Python', constants.s_player, creature=creature_com1)

    creature_com2 = com_Creature('Jackie', death_function=death_monster)
    ai_com = ai_Test()
    ENEMY = obj_Actor(10, 5, 'Crabby', constants.s_enemy, creature=creature_com2, ai=ai_com)

    creature_com3 = com_Creature('Pumba', death_function=death_monster)
    ai_com3 = ai_Test()
    ENEMY1 = obj_Actor(5, 5, 'Crabby', constants.s_enemy, creature=creature_com3, ai=ai_com3)

    creature_com4 = com_Creature('Ebalo', death_function=death_monster)
    ai_com4 = ai_Test()
    ENEMY2 = obj_Actor(5, 7, 'Crabby', constants.s_enemy, creature=creature_com4, ai=ai_com4)

    GAME_OBJECTS = [PLAYER, ENEMY, ENEMY1, ENEMY2]


def game_handle_keys():
    events_list = pygame.event.get()
    # Процесс ввода
    for event in events_list:
        if event.type == pygame.QUIT:
            return 'QUIT'

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PLAYER.creature.move(0, -1)
                return 'player-moved'
            if event.key == pygame.K_DOWN:
                PLAYER.creature.move(0, 1)
                return 'player-moved'
            if event.key == pygame.K_LEFT:
                PLAYER.creature.move(-1, 0)
                return 'player-moved'
            if event.key == pygame.K_RIGHT:
                PLAYER.creature.move(1, 0)
                return 'player-moved'

    return 'no-action'


#  _______ ___   ___  _______   ______      _______      ___      .___  ___.  _______
# |   ____|\  \ /  / |   ____| /      |    /  _____|    /   \     |   \/   | |   ____|
# |  |__    \  V  /  |  |__   |  ,----'   |  |  __     /  ^  \    |  \  /  | |  |__
# |   __|    >   <   |   __|  |  |        |  | |_ |   /  /_\  \   |  |\/|  | |   __|
# |  |____  /  .  \  |  |____ |  `----.   |  |__| |  /  _____  \  |  |  |  | |  |____
# |_______|/__/ \__\ |_______| \______|    \______| /__/     \__\ |__|  |__| |_______|

if __name__ == '__main__':
    game_initialization()
    game_main_loop()
