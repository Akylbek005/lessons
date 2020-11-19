# # from subprocess import Popen, PIPE
# # import os
# # import sys
# # import math
# # import requests
# # from argument import *
#
#
# def fun():
#     pass
#
#
# a = 1
#
# tuple_ = (
#     '1-value',
#     '1-value',
#     '2-value',
#     '3-value',
#     '4-value',
#     '5-value',
#     '6-value',
#     '7-value',
#     '8-value',
#     '9-value')
#
# mi_list = [
#     1, 2, 3,
#     4, 5, 6,
#     7, 8, 9,
# ]
# name = {'name':'Jon', 'name1':'Google'}
# x = 1 + 2
#
#
# def fun1(x, y):
#     return x + y
#
# fun1(1, 2)
#
# name ['name23'] = 'Akylbek'
#
#
# # функция складывает два числа!
# def add(x, y =10):
#     return x - 10
#
#
#
# heloo  = []
# print(heloo)
#
# class MyProfile():
#     pass
#
#
# class User():
#     pass
#
#
# def my_profile():
#     pass
#
#
# PI = 3.14
#
# my_profile2 = ''
#
# if my_profile2 == False:  #don't' True
#     pass
#
#
# if my_profile2 is True:
#     pass

# import math
#
# Pi = math.pi
# print(Pi)
#
# print(math.ceil(Pi)) #в нижнию
# print(math.floor(Pi)) #в верхнию
#
# num = -120
# print(abs(num)) # do pologitelny


import random

# print(random.randint(1, 100)) # от и до
# print(random.random()) # ot 0 do 0.9999...
# print(random.uniform(0, 10)) #число дробное

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(random.choice(li))
#
# random.shuffle(li)
# print(li)

# import  #ctatictika
#
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# res = int(sum(li)) / len(li)
#
# print(statistics.mean(li))
# print(res)




# import datetime # Классф для работы с датой\временем
# import time #функции для работы с веменем
# import calendar # для работы с календарем
# # import pytz\(res)e
#
# # print(datetime.datetime.now())
# # time.sleep(8)
# # print(datetime.date(2020, 11, 2))
# # print(datetime.datetime.now())
#
# year = [2015, 2016,2017, 2018, 2019, 2020]
# month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
# day =[i for i in range(1, 31)]
#
# print(datetime.date(year[0], month[0], day[0]))
# print(datetime.datetime.today())
# print(datetime.datetime.utcnow())


import sys          # Переменные и функцииб которые ипользуются с интерпретатаром
import platform     # Низко уровневая информация о платформе
import os           # Способ доступа к системе функции для разных платформ
import shutil       # Высокоуревнве операции с файлами (коированиеб удаление и т.д)
import subprocess   # Запуск процесса присоединение к потоком их ввода и вывода и получение кода внутри возврата

# print(platform.machine())     #
# print(platform.node())        #
# print(platform.processor())   #
# print(platform.system())      #
# print(platform.version())     #
# print(platform.uname())       #

# print(sys.platform)
# print(sys.maxsize)

os.mkdir('New_proeck')
# shutil.copy('t.txt', 'New_proeck')

# print(os.path.getsize('venv'))
