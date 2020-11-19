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

# 2
# class Employee:
#     def __init__(self, name, lastname, postition, salary):
#         self.name = name
#         self.lastname = lastname
#         self.postition = postition
#         self.salary = salary
#
#     def get_info(self):
#         print(f"{self.name} {self.lastname} работает на должности {self.postition} и получает  {self.salary} сомов.")
#
# a = Employee(input('Как вас зовут:'), input("Ваше фамилие:"), input('Ваша должность:'), input('Ваша зарплата:'))
# a.get_info()

# 3
# class Child:
#     def __init__(self, name, a, al):
#         self.name = name
#         self.a = a
#         self.al = input()
#         al1 = self.a * self.name
#         print(al1)
#         asd = al1 + self.al
# class Child1(Child):
#     def all1(self):
#         al = self.a * self.name
#         print(al)
#
# b = Child1(int(input('Input:')),int(input('input num:'), input())))
# b.all1()



# 4
# class Person():
#     def __init__(self, name, lastname, year_birth):
#         self.lastname = lastname
#         self.name = name
#         self.year_birth = year_birth
#
#     def get_age(self):
#         print(f"{self.lastname} {self.name} вам {self.year_birth} лет ")
#
# a = Person(input(), input(), 2020 -  int(input()))
# a.get_age()

# 5
class Animal:
    name = ''
    hunger = 6

    # def eat(self):


class Cat(Animal):
    def meow(self):
        if self.hunger > 5:
            print('Мияу!')
            life_lose = self.hunger - 1


class Dog(Animal):
    def bark(self):
        if self.hunger > 5:
            print('Гаф Гаф!')
            life_lose = self.hunger - 1


def main(Animal):
    name = input('как назавем')
    nam = Animal(name)





