# class List:
#     name = 'default'
#     contact = 'default'
#     address = 'default'
#
#     def set_(self, name, contact, address):
#         self.name = name
#         self.contact = contact
#         self.address = address
#
#
# kirill  = List()
# kirill.set_('kirill', '07733123773', 'Ak tuz')
# k = kirill = (kirill.name , kirill.contact , kirill.address)
#
# erkin = List()
# erkin.set_('erkin', '07733123773', 'Ak tuz')
# e = erkin = (erkin.name , erkin.contact , erkin.address)
#
# class ConList(List):
#     name = "erkin"
#
#     def search(self, name):
#         self.name = 1
#
#
# all_con = [kirill, erkin]
# all_con = ConList()
# all_con.search(1)
#
# # for i in range(0, 2):
# #     all_con.name = input()
# #
# #     if all_con.name == 'kirill':
# #         print(k)
# #
# #     if all_con.name == 'erkin':
# #         print(e)
#
#
# for i in range(0, 2):
#     all_con.name = input()
#
#     if all_con.name in e:
# #         print(e)
# #     if all_con.name in k:
# #         print(k)
#
#
#
# class House:
#     mebel = 'default'
#     s = '85'
#     def __init__(self,s):
#         self.s = s
# class Furn(House):
#     def abc(self, locker, table, bed):
#
#         self.locker = locker
#         self.table = table
#         self.bed = bed
#
#
# s = int(input('Введите площадь квартиры:'))
# table = int(input('Площадь стола:'))
# locker = int(input('Площадь шкафа:'))
# bed = int(input('Площадь кровати:'))
# a = Furn(s)
# a.abc(table, locker, bed)
# print(f'Площадь квартиры: {a.s},\nсписков мебели внутри: кровать, стол, шкаф')
#
# abc = (a.s - (a.locker + a.bed + a.table))
#
# if abc > 0:
#     print(f'Осталось всего {abc} кв.м')
#
# else:
#     print('Мест для мебели нету')


# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     def __hash__(self):
#         return hash(self.email)
#
#     def __eq__(self, obj):
#         return self.email == obj.email
#
# Jon = User('Lon Conor',' jon@gmail.com')
# Sonya = User('Somya blad', 'sonya@gmail.com')
#
# print(hash(Jon.email))
# print(hash(Sonya.email))

# class Res:
#     def __getattr__(self, name):
#         return 'Nothing Found :('
#
#     def __getattribute__(self, name ):
#         print(f'Looking for {name}')
#         return 'nope'
#
# obj = Res()
#
# print(obj.attr)
# print(obj.method)
# print(obj.DFG2H3JLL)


# class A:
#     def __setattr__(self, name ,value ):
#         print(f"Not gonna det {name}")
#
# obj = A()
# obj.name  = True


# class Polit:
#     def __delattr__(self, name):
#         value = getattr(self, name)
#         print(f"Goodbye {name}, you were {value}!")
#         object.__delattr__(self, name)
#
# obj = Polit()
# obj.attr = 10
# del obj.attr


# class Logger:
#     def __init__(self, fname):
#         self.fname = fname
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             with open(self.fname, 'a') as f :
#                 f.write('Oh Danny boy ...')
#
#             return func(*args, **kwargs)
#         return wrapper
#
# logger = Logger('index.txt')
# @logger
# def copyk():
#     pass


# import random
# class Noisy:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, obj):
#         noise = random.uniform(-1, 1)
#         return self.value + obj.value + noise
#
# a = Noisy(10)
# b = Noisy(20)
#
# for _ in range(10):
#     print(a + b )

# class Pascal:
#     def __init__(self, original_list = None):
#         self.container = original_list or []
#
#     def __getitem__(self, index):
#         return self.container[index - 1]
#
#     def __setitem__(self, index, value):
#         self.container[index - 1] = value
#
#     def __str__(self):
#         return  self.container.__str__()
#
# numbers = Pascal([1,2,3,4,5,6,7,8,9,10])
# print(numbers[-6])










