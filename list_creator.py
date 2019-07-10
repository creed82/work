import pyperclip

filename = input('Введи название словаря/списка: ')
f = open('{}.txt'.format(filename), 'w')

your_list = []
your_dict = {}


def copy():
    f = open('{}.txt'.format(filename), 'r')
    for row in f:
        pyperclip.copy(row)
    boofer = pyperclip.paste()
    f.close()


def list_creator():
    while True:
        input_user = input('Введи значение: ')
        if input_user == '':
            break
        else:
            your_list.append(input_user)
    f.write(filename + '=' + str(your_list))
    f.close()
    copy()
    print('я сгенерил лист' + str(your_list))


def dict_creator():
    while True:
        input_user = input('Введи ключ: ')
        if input_user == '':
            break
        else:
            value = input('Введи значение для ключа: ')
            your_dict.setdefault(input_user, str(value))  # Если нужны числа, 2 аргумент str поменяй на int
    f.write(filename + '=' + str(your_dict))
    f.close()
    copy()
    print('я сгенерил словарик' + str(your_dict))


ask = input('Что хочешь сгенерировать список или словарь? l/d: ')
if ask == 'l' or ask == 'L' or ask == 'л' or ask == 'Л' or ask == 'list':
    print('Оставь поле пустым чтобы завершить программу.')
    list_creator()
if ask == 'd' or ask == 'D' or ask == 'dict' or ask == 'д' or ask == 'Д':
    print('Оставь поле пустым чтобы завершить программу.')
    dict_creator()
