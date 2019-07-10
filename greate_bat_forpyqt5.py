import os

print("""Привет! Эта прога поможет тебе создать два бат файла
для перезагрузки GUI твоих проектов и для компиляции конечного файла в exe.
Так же она создаст _main.py для твоего GUI со всеми необходимыми импортами""")
print('-------------------------------------------------------------------------')
print("Вводить надо только имя без разрешения .ui")
player_input = input('Введи название ui файла: ')

redact = open('{}_reload.txt'.format(player_input), 'w')
redact.write('pyuic5 {}.ui -o {}.py'.format(player_input, player_input))
redact.close()
os.rename('{}_reload.txt'.format(player_input), '{}_reload.bat'.format(player_input))

redact = open('{}_main.txt'.format(player_input), 'w')
redact.write("""
# -*- coding: utf-8 -*-
# Imports
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from {} import Ui_MainWindow""".format(player_input))
redact.write("""
# Window initialization
app = QtWidgets.QApplication(sys.argv)
{} = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi({})
{}.show()

# Your Code Here


sys.exit(app.exec_())
""".format(player_input, player_input, player_input))
redact.close()
os.rename('{}_main.txt'.format(player_input), '{}_main.py'.format(player_input))

redact.close()

redact = open('{}_compilate.txt'.format(player_input), 'w')
redact.write('pyinstaller -w -F {}.py'.format(player_input))
redact.close()
os.rename('{}_compilate.txt'.format(player_input), '{}_compilate.bat'.format(player_input))

os.system('C:/Projects/work/{}_reload.bat'.format(player_input))

