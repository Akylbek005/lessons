# class Dog():
#
#     def __init__(self, size, name):
#         self.size = size
#         self.name = name
#
#     def speak(self):
#         if self.size == 'small':
#             print('ЭТо маленькая собака!')
#         elif self.size == 'middle':
#             print('Это средняя собака!')
#         elif self.size == 'large':
#             print('Это большая собака')
#
#
# class Doberman(Dog):
#     def __init__(self, name, size ='large'):
#         self.name = name
#         self.size = size
#     def speak(self):
#         print('Это собака породы доберман')
#
# rex = Doberman('Rex')
# rex.speak()
#
# bobik = Dog("middle", 'Bobik')
# bobik.speak()

# class Pet:
#     def __init__(self, name, age ):
#         self.name = name
#         self.age = age
#         print('Появился новый питомец, работае метод __init__')
#
#
#     def talk(self):
#         print(' . . . . .')
#
#
# class Fish(Pet):
#     def __init__(self, name, age, color):
#         self.name = name
#         self.color = color
#         self.age = age
#         print("Появился новоая рыба")
#
#
# class Cat(Pet):
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age  = age
#         self.breed = breed
#         print('Появился новый кот работае метод --__init__')
#
#     def talk(self):
#         print('Мияу')
#
# class Turtle(Pet):
#     def run(self, x, y):
#         self.x = x
#         self.y = y
#         print(f'Черепаха пробежала {self.x + self.y} километров')
#
#
# class Dog(Pet):
#     def __init__(self, name, age, breed, size):
#         self.name = name
#         self.age  = age
#         self.breed = breed
#         self.size = size
#         print('Появился новая собака работае метод __init__')
#
#
#     def speak(self):
#         if self.size == 'little' or self.size == 'medium':
#             print('Гав')
#         else:
#             print('woof')
#
#
# dori = Fish('Дори','1','черный')
# dori.talk()
# rex = Dog('gray', 3, 'doberman', 'medium')
# gray = Dog("gray", 2 , 'dashung', 'little')
# tom = Cat('Tom',3,'mainkun')
# rex.speak()
# gray.talk()
# tom.talk()
# donotello = Turtle('donotello', 7)
# donotello.run(2, 5)








