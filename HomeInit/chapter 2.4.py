# # # декоратор
#
# def burger(func):
#     def bur(*arg,**argu):
#         print('Вверхняя булочка')
#         func(*arg,**argu)
#         print('Нижняя булочка')
#     return bur
#
# def kotlet(k):
#     def kot(*arg,**argu):
#         print("курочка")
#         k(*arg,**argu)
#         print("говядина")
#     return kot
#
# @burger
# @kotlet
# def nachnka(sir,pomidor,sous,salat):
#     print('\n',sir,'\n',pomidor,'\n',sous,'\n',salat)
# nachnka('Сыр',"помидор","соус","салат")

# def burger(func):
#     def bur(*arg,**argu):
#         print('Крыша')
#         func(*arg,**argu)
#         print('Фундамент')
#     return bur()
#
#
#
# def kotlet(k):
#     def kot(*arg,**argu):
#         print('7ой этаж')
#         k(*arg,**argu)
#         print('1ый этаж')
#     return kot()
#
# @burger
# @kotlet
# def nachnka(sir,pomidor,sous,salat):
#     print('\n',sir,'\n',pomidor,'\n',sous,'\n',salat)
# nachnka('Сыр',"помидор","соус","салат")


# 2 ой номер
# print('Сколько будет 2 + 2 * 2 = ?')
# use1 = int(input('Ваш ответ:'))
# if use1 == 6:
#     user1 = (f'Ваш ответ: 2 + 2 * 2 = {use1} правильный')
# else:
#     user1 = (f'Ваш ответ: 2 + 2 * 2 = {use1} не верный!')
# print('Сколько будет 10 / 10 * 1 = ?')
# use2 = int(input('Ваш ответ:'))
# if use2 == 1:
#     user2 = (f'Ваш ответ: 10 / 10 * 1 = {use2} праильный')
# else:
#     user2 = (f'Ваш ответ: 10 / 10 * 1 = {use2} не венрый! ')
#
#
# def matem1(func):
#     def resh(*arg, **argu):
#         print('')
#         func(*arg, **argu)
#     return resh
#
#
# def matem2(func):
#     def resh(*arg, **argu):
#         print('')
#         func(*arg, **argu)
#     return resh
# @matem1
# @matem2
# def hi (bot1, user1, bot2, user2):
#     print('\n',bot1 ,'\n', user1,"\n", bot2 ,'\n', user2)
# hi(f'Правильный результат: 2 + 2 * 2 = 8',user1, 'Правильный результат: 10 / 10 * 1 = 1', user2)




