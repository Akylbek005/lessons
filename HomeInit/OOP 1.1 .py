# 1
# class Shop:
#     name = input('Напишите имя магазина:')
#     is_open = input('Введите продукт которой хотите купить!')
#     product_list = ['яблоко',"груша","колбаса","вода"]
#     def open_produck(self):
#         if self.is_open in self.product_list:
#             self.is_open = 'True'
#             print(self.is_open)
#         else:
#             self.is_open = 'False'
#             print(self.is_open)
#
#     def add_product(self):
#         pass
#
#     def is_available(self):
#         pass
#
#     def buy_product(self):
#         pass
#
# user = Shop()
# user.open_produck()





# class Animal:
#     def __init__(self, name, hunger = 6):
#         self.name = name
#         self.hunger = hunger
#
#     def eat(self, food = 1):
#         self.hunger += food
#         print('Животное ест')
#
#     def status(self):
#         print(f'hunger of {self.name}:{self.hunger}')
#
# class Cat(Animal):
#     def meow(self):
#         if self.hunger > 5:
#             self.hunger -= 1
#             print('moew')
#         else:
#             print(f'hunger = {self   .hunger}')
#
# class Dog(Animal):
#     def bark(self):
#         if self.hunger > 5:
#             self.hunger -= 1
#             print('Woof')
#         else:
#             print(f'hunger = {self   .hunger}')
#
# dog = Dog('dog')
# dog.status()
# dog.eat()
# dog.bark()
# dog.status()
# cat = Cat('Tom', 3)
# cat.status()
# cat.meow()
# cat.eat(4)
# cat.status()


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def breathe(self):
#         print('Дышит')
#
#     def move(self):
#         print('Двигается')
#
#     def eat(self):
#         print('Ест')
#
# class Mammals(Animal):
#     def feed_kids_milk(self):
#         print('Кормят детенышей молоком ')
#
#
# class Giraffes(Mammals):
#     def eat_trees(self):
#         print('Едят листья')
#
#     def move(self):
#         print('Жираф передвигается')
#
# melman = Giraffes('Melman')
# melman.breathe()
# melman.feed_kids_milk()
# melman.eat()
# melman.eat_trees()
# melman.move()


# class Car:
#     def __init__(self, make, model, year, odometer = 0, fuel = 70):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = odometer
#         self.fuel = fuel
#
#     def drive(self):
#         km = int(input())
#         toplivo = 70 / km - 10 / 100
#         if 70 / km > 10 /100:
#             def _add_distance(self):
#                 self.odometer = km
#
#                 def _subtruck_fuel(self):
#                     self.fuel -= toplivo
#                     print('Lets drive')
#         elif 70 / km < 10 / 100:
#             print('Need for fuel')
#
#
# bmv = Car('Germany', 'x6', 2017 )
# bmv.drive()
# bmv._add_distance()


# class Car():
#     def __init__(self, make, model, year, odometer=0, fuel=70):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = odometer
#         self.fuel = fuel
#
#     def drive(self, distance):
#         self.distance = distance
#         self.distance = int(input())
#
#         if distance/10 <= self.fuel:
#             def _add_distance(self):
#                 self.odometr += self.distance
#
#             def _subtract_fuel(self):
#                 self.fuel -= distance/10
#
#             print('Lets Drive!')
#         else:
#             print('Need more fuel, please, fill more!')
#
# car1 = Car("germany",'bmw','2018' )
# car1.drive(500)






