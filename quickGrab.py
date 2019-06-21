hero_list = []


class Hero():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def show(self):
        print(self.name, self.role)


hero_1 = Hero(input('Введите имя героя: '), input('Введите класс героя: '))
hero_list.append(hero_1)

hero_2 = Hero('sasha', 'warrior')
hero_list.append(hero_2)

hero_3 = Hero('artem', 'rouge')
hero_list.append(hero_3)

for i in hero_list:
    i.show()
