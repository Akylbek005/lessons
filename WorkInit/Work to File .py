# list_ = [num for num in range(1,51)]
#
# with open('test.txt', 'w') as f:
#     for i in list_:
#         f.write(str(i)+'\n')
#
# with open('test.txt', "r") as file:
#     for line in file:
#         print(line)
#
# # соединят файлы
# text = 'hello world'
# write_f = open('test.txt', "a")
# write_f.write(text)
# write_f.close()
#
#
# import os
# удаляет файл
# os.remove('/home/akylbek/PycharmProjects/pythonProject/test.txt')
# os.rename('/home/akylbek/PycharmProjects/pythonProject/test.txt', '/home/akylbek/PycharmProjects/pythonProject/test.txt')

# Ошибки
# list_ = [num for num in range(1,51)]
#
# try:
#     with open('test.txt', 'w') as f:
#         for i in list_:
#             f.write(i + '\n')
# except TypeError:
#     print('Error')
#
# print('code working')

# try:
#     num = 1 / 0
#     print(num)
# except NameError as error:
#     print(error)
#     num = 0
#
# print("На ноль делить нельзя")

# f = open('test.txt')
# nums = []
# try:
#     for i in f:
#         nums.append(int(i))
# except ValueError:
#     print('Это не число')
# except Exception:
#     print('Что это такое')
# else:
#     print('Все работает!')
# finally:
#     f.close()
#     print("Я закрыл файл")
#     print(nums)






