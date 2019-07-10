import random
import time

print('Кнопка "i" откроет окно персонажа')
print('Кнопка "h" позволит выпить зелье здоровья')
# Переделать систему статов str(25) для функции итемов
# добавить словарь с итемами
# добавить список с лутом и инвертарем
# Игра
dice_game = random.randint(1, 6)

# Статы героя
hero_stamina = 5  # одно очко стамины дает +3 хп
hero_strength = 5  # одно очко силы дает +1 хп и + 1 катаке
hero_agility = 5  # одно очко ловкости дает +2 урона к атаке
hero_intellect = 5  # одно очко интеллекта дает + 3 к мане
# Показатели героя
hero_xp = 0
hero_max_xp = 100
hero_lvl = 1
hero_hp_max = hero_stamina * 3
hero_hp = hero_hp_max
hero_mp_max = hero_intellect * 3
hero_mp = hero_mp_max
hero_armor = 1
hero_damage = hero_strength * 1
# Статы врага
enemy_stamina = 5  # одно очко стамины дает +3 хп
enemy_strength = 5  # одно очко силы дает +1 хп и + 1 катаке
enemy_agility = 5  # одно очко ловкости дает +2 урона к атаке
enemy_intellect = 5

enemy_lvl = 1
enemy_hp_max = enemy_stamina * 3
enemy_hp = enemy_hp_max
enemy_mp_max = enemy_intellect * 3
enemy_mp = enemy_mp_max
enemy_armor = 1
enemy_damage = enemy_strength * 1
# Предметы и инвентарь
item_helmet = ''
item_body_armor = ''
item_gloves = ''
item_pants = ''
item_trinket = ''
item_weapon = ''
heal_potions = 2
heal_cast_count = 1
hero_gold = 0

mods = ('обычный','необычный', 'редкий', 'уникальный')


def enemy_spawn():
    global enemy_lvl, enemy_stamina, enemy_strength, enemy_agility, enemy_intellect, enemy_hp_max, \
        enemy_hp, enemy_mp_max, enemy_mp, enemy_damage, enemy_armor, hero_lvl, hero_stamina, hero_strength, \
        hero_agility, hero_intellect, hero_hp_max, hero_hp, hero_mp_max, hero_mp, hero_damage, hero_armor
    rarity = random.choice(mods)
    if rarity == 'обычный':
        enemy_stamina = hero_stamina + random.randint(-3, +0)
        enemy_strength = hero_strength + random.randint(-3, +0)
        enemy_agility = hero_agility + random.randint(-3, +0)
        enemy_intellect = hero_intellect + random.randint(-3, +0)
        enemy_lvl = hero_lvl
        enemy_hp_max = enemy_stamina * 3
        enemy_hp = enemy_hp_max
        enemy_mp_max = enemy_intellect * 3
        enemy_mp = enemy_mp_max
        enemy_armor = hero_lvl
        enemy_damage = enemy_strength * 1
    elif rarity == 'необычный':
        enemy_stamina = hero_stamina + random.randint(-1, +1)
        enemy_strength = hero_strength + random.randint(-1, +1)
        enemy_agility = hero_agility + random.randint(-1, +1)
        enemy_intellect = hero_intellect + random.randint(-1, +1)
        enemy_lvl = hero_lvl
        enemy_hp_max = enemy_stamina * 3
        enemy_hp = enemy_hp_max
        enemy_mp_max = enemy_intellect * 3
        enemy_mp = enemy_mp_max
        enemy_armor = hero_lvl
        enemy_damage = enemy_strength * 1
    elif rarity == 'редкий':
        enemy_stamina = hero_stamina + random.randint(+1, +3)
        enemy_strength = hero_strength + random.randint(+1, +3)
        enemy_agility = hero_agility + random.randint(+1, +3)
        enemy_intellect = hero_intellect + random.randint(+1, +3)
        enemy_lvl = hero_lvl
        enemy_hp_max = enemy_stamina * 3
        enemy_hp = enemy_hp_max
        enemy_mp_max = enemy_intellect * 3
        enemy_mp = enemy_mp_max
        enemy_armor = hero_lvl
        enemy_damage = enemy_strength * 1
    elif rarity == 'уникальный':
        enemy_stamina = hero_stamina + random.randint(+5, +9)
        enemy_strength = hero_strength + random.randint(+3, +7)
        enemy_agility = hero_agility + random.randint(+3, +7)
        enemy_intellect = hero_intellect + random.randint(+3, +7)
        enemy_lvl = hero_lvl
        enemy_hp_max = enemy_stamina * 3
        enemy_hp = enemy_hp_max
        enemy_mp_max = enemy_intellect * 3
        enemy_mp = enemy_mp_max
        enemy_armor = hero_lvl
        enemy_damage = enemy_strength * 1
    print('Уровень монстра:             ' + str(enemy_lvl))
    print('Редкость монстра:            ' + str(rarity))
    print('Уровень здоровья:            ' + str(enemy_hp) + '/' + str(enemy_hp_max))
    print('Урон монстра:                ' + str(enemy_damage))
    print('Уровень брони монста:        ' + str(enemy_armor))



def hero_lvl_up():
    '''повышаем уровень героя'''
    global hero_hp, hero_xp, hero_max_xp, hero_lvl, hero_hp_max, hero_stamina, hero_strength, hero_agility, hero_intellect
    if hero_xp <= hero_max_xp:
        hero_xp += 25
        print('Вы получили 25 единиц опыта')
        if hero_xp >= hero_max_xp:
            hero_xp = 0
            hero_lvl += 1
            hero_stamina += 1
            hero_strength += 1
            hero_agility += 1
            hero_intellect += 1
            print('Поздравляем вы достигли ' + str(hero_lvl) + ' уровня!')
        else:
            pass


def hero_stats(leftWidht, rightWidht):
    # выводим на экран фразу 'Picnic items' и выравниваем по центру(левая сторона, правая сторона, пустоты заполним "-"
    print('Информация о герое:'.center(leftWidht + rightWidht, '-'))
    print('Уровень персонажа:             ' + str(hero_lvl))
    print('Уровень текущего опыта:        ' + str(hero_xp) + '/' + str(hero_max_xp))
    print('Уровень здоровья:              ' + str(hero_hp) + '/' + str(hero_hp_max))
    print('Уровень брони:                 ' + str(hero_armor))
    print('Уровень атаки:                 ' + str(hero_damage))
    print('Зелья здоровья:                ' + str(heal_potions + 1))
    print('Предметы'.center(leftWidht + rightWidht, '-'))
    print('Оружие:  ' + str(item_weapon))
    print('Голова:  ' + str(item_helmet))
    print('Тело:    ' + str(item_body_armor))
    print('Руки:    ' + str(item_gloves))
    print('Ноги:    ' + str(item_pants))
    print('Амулет:  ' + str(item_trinket))
    print('-'.center(leftWidht + rightWidht, '-'))


def user_input_key():
    #  Тут отслеживается нажатия пользователя
    # тут же можно отрубить ходы при вводе пустого поля (сейчас все срабатывает автоматом)
    global user_input, hero_hp, hero_hp_max, heal_potions, dice_game
    if user_input == 'h' or user_input == 'H' or user_input == 'р' or user_input == 'Р':
        if heal_potions >= 0:
            if hero_hp >= hero_hp_max:
                hero_hp = hero_hp_max
                print('У вас полное здоровье!')
            else:
                hero_hp += 15
                print('Герой захилился на 15 хп')
                heal_potions -= 1
        else:
            print('Зелий здоровья больше нет...')

    elif user_input == 'i' or user_input == 'I' or user_input == 'ш' or user_input == 'Ш':
        hero_stats(20, 20)


def hero_hp_loss():
    global hero_hp, hero_armor, enemy_damage
    hero_hp -= (enemy_damage - (int(hero_armor * 0.3)))
    print('Монстр наносит вам: ' + str(enemy_damage - (int(hero_armor * 0.3))) + ' урона.')


def enemy_hp_loss():
    global enemy_hp, hero_damage, enemy_armor
    enemy_hp -= (hero_damage - (int(enemy_armor * 0.3)))
    print('Вы наносите монстру: ' + str(hero_damage - (int(enemy_armor * 0.3))) + ' урона.')


game = True

while game:
    if hero_hp <= 0:
        print("Вы погибли... Игра окончена")
        break
    else:
        print()
        user_input = input("Бросьте кости для следующего действия!")
        print()
        user_input_key()
        if user_input == '':
            dice_game = random.randint(1, 6)
            print()
            print('Бросаем кость...')
            print('На костях выпало: ' + str(dice_game))
            print()
            if dice_game == 1 or dice_game == 4:
                enemy_spawn()
                fight_with_enemy = True
                while fight_with_enemy:
                    user_input = input("----------------------------------------")
                    user_input_key()
                    if user_input == '':
                        dice_game = random.randint(1, 6)
                        # 1. Обычная атака
                        if dice_game == 1:
                            print('Вы проводите обычную атаку.')

                            hero_hp_loss()
                            enemy_hp_loss()
                            print("Ваше здоровье:  " + str(hero_hp) + "  |  " + "Здоровье врага:  " + str(enemy_hp))
                            if hero_hp <= 0:
                                break
                            elif enemy_hp <= 0:
                                hero_lvl_up()
                                break

                        # 2. Блок урона
                        elif dice_game == 2:

                            print('Вы блокируте 30% входящего урона от: ' + str(enemy_damage))
                            blocked_damage = int((enemy_damage - (hero_armor * 0.3)) * 0.7)
                            hero_hp -= blocked_damage
                            print('Враг наносит вам: ' + str(blocked_damage) + ' урона.')
                            print("Ваше здоровье:  " + str(hero_hp) + "  |  " + "Здоровье врага:  " + str(enemy_hp))
                            if hero_hp <= 0:
                                break
                            elif enemy_hp <= 0:
                                hero_lvl_up()
                                break

                        # 3. Критическая атака
                        elif dice_game == 3:

                            enemy_hp -= hero_damage * 2
                            print('Вы ощутили прилив сил...')
                            print('и проводите критическую атаку! Враг теряет здоровья: ' + str(hero_damage * 2))
                            hero_hp -= (enemy_damage - (int(hero_armor * 0.3)))
                            print('Враг наносит вам: ' + str(enemy_damage - (int(hero_armor * 0.3))) + ' урона.')
                            print("Ваше здоровье:  " + str(hero_hp) + "  |  " + "Здоровье врага:  " + str(enemy_hp))
                            if hero_hp <= 0:
                                break
                            elif enemy_hp <= 0:
                                hero_lvl_up()
                                break

                        # 4. Уклонение
                        elif dice_game == 4:

                            print('Вы уклонились от входящего урона')
                            print('Враг наносит вам: 0 урона.')
                            print("Ваше здоровье:  " + str(hero_hp) + "  |  " + "Здоровье врага:  " + str(enemy_hp))
                            if hero_hp <= 0:
                                break
                            elif enemy_hp <= 0:
                                hero_lvl_up()
                                break

                        # 5. Контр-Атака
                        elif dice_game == 5:

                            enemy_hp -= int(hero_damage * 0.75)
                            print('Вы контратакуете врага, он теряет здоровья: ' + str(int(hero_damage * 0.75)))
                            print('Враг наносит вам: 0 урона.')
                            print("Ваше здоровье:  " + str(hero_hp) + "  |  " + "Здоровье врага:  " + str(
                                enemy_hp))
                            if hero_hp <= 0:
                                break
                            elif enemy_hp <= 0:
                                hero_lvl_up()
                                break


                        # 6. Промах
                        elif dice_game == 6:

                            enemy_hp -= 0
                            print('Вы промахиваетесь.')
                            hero_hp -= (enemy_damage - (int(hero_armor * 0.3)))
                            print('Враг наносит вам: ' + str(enemy_damage - (int(hero_armor * 0.3))) + ' урона.')
                            print("Ваше здоровье:  " + str(hero_hp) + "  |  " + "Здоровье врага:  " + str(enemy_hp))
                            if hero_hp <= 0:
                                break
                            elif enemy_hp <= 0:
                                hero_lvl_up()
                                break

            elif dice_game == 2:
                print("Вы находите сундук!")
                treasure_chest = True
                while treasure_chest:
                    user_input = input("------------------------------------------------")
                    user_input_key()
                    if user_input == '':
                        dice_game = random.randint(1, 6)

                        if dice_game == 1:
                            print("Вы нашли шлем")
                            if item_helmet == '':
                                # добавить замену шлемака и проверку
                                item_helmet = 'Простой шлем солдата'
                                hero_hp_max += 5
                                hero_hp += 5
                                hero_armor += 1
                                print('Простой шлем солдата')
                                print('Увеличивает ваш уровень здоровья на 5 единиц.')
                                print('Увеличивает вашу броню на 1.')
                                treasure_chest = False
                            else:
                                print('У вас уже есть Простой шлем солдата')
                                treasure_chest = False
                        elif dice_game == 2:
                            print("Вы нашли Простой броник солдата")
                            if item_body_armor == '':  # ЗДЕСЬ ДРУГОЙ ИТЕМ
                                # добавить замену шлемака и проверку
                                item_body_armor = 'Простой броник солдата'
                                hero_hp_max += 15
                                hero_hp += 15
                                hero_armor += 3
                                print('Простой броник солдата')
                                print('Увеличивает ваш уровень здоровья на 15 единиц.')
                                print('Увеличивает вашу броню на 3.')
                                treasure_chest = False
                            else:
                                print('У вас уже есть Простой броник солдата')
                                treasure_chest = False
                        elif dice_game == 3:
                            print("Вы нашли Простые перчатки солдата")
                            if item_gloves == '':
                                # добавить замену шлемака и проверку
                                item_gloves = 'Простые перчатки солдата'
                                hero_hp_max += 5
                                hero_hp += 5
                                hero_armor += 1
                                hero_damage += 1
                                hero_damage += 1
                                print('Простые перчатки солдата')
                                print('Увеличивает ваш уровень здоровья на 5 единиц.')
                                print('Увеличивает вашу броню на 1.')
                                print('Увеличивает атаку на 1.')
                                treasure_chest = False
                            else:
                                print('У вас уже есть Простые перчатки солдата')
                                treasure_chest = False
                        elif dice_game == 4:
                            print("Вы нашли Простые штаны солдата")
                            if item_pants == '':
                                # добавить замену шлемака и проверку
                                item_pants = 'Простые штаны солдата'
                                hero_hp_max += 5
                                hero_hp += 5
                                hero_armor += 2
                                print('Простые перчатки солдата')
                                print('Увеличивает ваш уровень здоровья на 5 единиц.')
                                print('Увеличивает вашу броню на 2.')
                                treasure_chest = False
                            else:
                                print('У вас уже есть Простые штаны солдата')
                                treasure_chest = False

                        elif dice_game == 5:
                            print("Вы нашли Простой амулет солдата")
                            if item_trinket == '':
                                # добавить замену шлемака и проверку
                                item_trinket = 'Простой амулет солдата'
                                hero_hp_max += 25
                                hero_hp += 25
                                print('Простой амулет солдата')
                                print('Увеличивает ваш уровень здоровья на 25 единиц.')
                                treasure_chest = False
                            else:
                                print('У вас уже есть Простой амулет солдата')
                                treasure_chest = False
                        elif dice_game == 6:
                            print("Вы нашли Простой меч солдата")
                            if item_weapon == '':
                                # добавить замену шлемака и проверку
                                item_weapon = 'Простой меч солдата'
                                hero_damage += 5
                                hero_damage += 9
                                print('Простой меч солдата')
                                print('Увеличивает вашу атаку в среднем на 7 единиц.')
                                treasure_chest = False
                            else:
                                print('У вас уже есть Простой меч солдата')
                                treasure_chest = False

            elif dice_game == 3:
                # Сделать стаки и улучшенные эффекты
                print("Вы находите Оскверенный алтарь!")
                user_input_key()
                pylon_effect = True
                while pylon_effect:
                    user_input = input("------------------------------------------------")
                    user_input_key()
                    if user_input == '':
                        dice_game = random.randint(1, 6)
                        print('Вы прикасаетесь к алтарю...')

                        if dice_game == 1:
                            time.sleep(0.5)
                            print('...')
                            print('Алтарь засиял от вашего прикосновения!')
                            time.sleep(0.5)
                            print('Вы стали мудрее и получили уровень!')
                            hero_lvl += 1
                            hero_hp_max += 10
                            hero_hp += 10
                            hero_damage += 1
                            hero_damage += 2
                            print('Поздравляем вы достигли ' + str(hero_lvl) + ' уровня!')
                            print('Уровень здоровья повышен на 10')
                            print('Урон повышен в среднем на 2')
                            pylon_effect = False

                        elif dice_game == 2:
                            time.sleep(0.5)
                            print('...')
                            print('Алтарь потемнел от вашего прикосновения! Вы стали чувствовать себя хуже.')
                            print('Ваш максимальный уровень здоровья понижен на 15 единиц.')
                            hero_hp_max -= 15
                            if hero_hp > hero_hp_max:
                                hero_hp = hero_hp_max
                            pylon_effect = False


                        elif dice_game == 3:
                            time.sleep(0.5)
                            print('...')
                            print('Алтарь покрылся кровью от вашего прикосновения...')
                            print('Вы потеряли 10 единиц здоровья, но стали сильнее.')
                            print('Ваш уровень атаки повышен на 3 единицы.')
                            hero_hp -= 10
                            hero_damage += 2
                            hero_damage += 4
                            pylon_effect = False

                        elif dice_game == 4:
                            time.sleep(0.5)
                            print('...')
                            print('Алтарь рассыпался в пыль от вашего прикосновения...')
                            print('Ваш доспех стал менее прочным. Вы потеряли 4 единицы брони')
                            hero_armor -= 4
                            if hero_armor <= 0:
                                hero_armor = 0
                                pylon_effect = False
                            else:
                                pylon_effect = False

                        elif dice_game == 5:
                            time.sleep(0.5)
                            print('...')
                            print('Алтарь осветил комнату от вашего прикосновения...')
                            print('Ваш запас здоровья и маны полностью восстановлен!')
                            hero_hp = hero_hp_max
                            hero_mp = hero_mp_max
                            pylon_effect = False

                        elif dice_game == 6:
                            time.sleep(0.5)
                            print('...')
                            print('Алтарь раскалился до красна от вашего прикосновения...')
                            print('Ваш запас здоровья повышен на 15 единиц и броня повышены!')
                            print('Ваш запас брони повышен на 3 единицы!')
                            hero_hp_max += 15
                            hero_armor += 3
                            pylon_effect = False
