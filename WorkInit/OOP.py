# class MyClass:
    # pass


# class Person():
#     pass
#
# Person.money = 150
#
#
#
# object1 = Person()
# object2 = Person()
# object1.name = 'Bob'
# object2.name = 'Carl'
# print(object1.name, 'has', object1.money,'dollars')
# print(object2.name, 'has', object2.money,'dollars')


# class Person:
#     name = ''
#     money = 0
#
#
# obj1 = Person()
# obj2 = Person()
#
# obj1.name = 'Bob'
# obj1.money = 200
# obj2.name = 'Carl'
# obj2.money = 300
#
# print(obj1.name, 'has', obj1.money, 'com')
# print(obj2.name, 'has', obj2.money, 'com')


# class Person:
#     name = ''
#     money = 0
#     def out(self): # self - Ссылка на обьект
#         print(self.name, 'has', self.money, ' dollars')
#
#     def changem(self, new_money):
#         self.money = new_money
#
# obj1 = Person()
# obj2 = Person()
#
# obj1.name = 'Bob'
# obj2.name = 'Carl'
#
# obj1.changem(180)
# obj2.changem(200)
#
# obj1.out()
# obj2.out()





# class Pet():
#     def __init__(self, name):
#         print('Появился новое животне Pet')
#         self.name = name
#
#
#     def __str__(self): # Возвращает строку которая содержит значени name
#         rep = 'Обьект класса Pet\n'
#         rep += 'Имя:' +  self.name +'\n'
#         return  rep
#
#
#     def talk(self):
#         print(f'Привет, я родился! Мое имя {self.name}\n')
#
# pet1 = Pet("Bobik")
# pet1.talk()
# pet2 = Pet('Sharik')
# pet2.talk()
# print(pet1)
# print(pet2)


# class Pet():
#     total = 0
#
#     @staticmethod
#     def status():
#         print(f'\n Всего животных сейчас {Pet.total}')
#
#
#     def __init__(self, name):
#         self.name = name
#         print('Появился нове животное')
#         Pet.total += 1
#
# print(Pet.total)
#
# pet1 = Pet('Bobik')
# pet2 = Pet('Aktosh')
# pet3 = Pet('Chupa')
# Pet.status()




# class A:
#     def _private(self):
#         print('This is private')
#
# a = A()
# a._private()




# class B:
#     def __privat(self):
#         print('Это закрытый метод')
#
# a = B()
# # a.__privat
#
# a._B__privat()



# class Pet():
#     def __init__(self, name, mood ):
#         print('Появился новое животное')
#         self.name = name
#         self.__mood = mood
#
#     def talk(self):
#         print('\Меня зовут ', self.name)
#         print('Сейчас я чуыстыую себя', self.__mood,"\n" )
#
#
#     def __privat_method(self):
#         print('Это закрытый метод')
#
#     def public_method(self):
#         print('Это открытый метод')
#         self.__privat_method()
#
# pet = Pet( name = "Bobik", mood = 'Good')
# pet.talk()
# pet.public_method()





class Pet():
    # Конструкция класса 3 открыых отрибутов
    def __init__(self, name, hunger = 0 , boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    # Закрытый метод увеличивающий чувство голода
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    # Свойсвто отражает самочувствии животного
    @property
    def mood(self):
        donthappy = self.hunger + self.boredom
        if donthappy < 5:
            m = "Прекрасно"
        elif 5 <= donthappy <= 10:
            m = 'Неплохо'
        elif 11 <= donthappy <= 15:
            m = 'так себе'
        else:
            m = 'Ужасно '
        return m

    # О сомочувствии животного
    def talk(self):
        print(f"Меня зовут: {self.name}")
        print(f'И я чувствую себя {self.mood}')
    # Снижает уровень голода животного
    def eat(self, food = 4):
        print('Спасибо')
        self.hunger -= food
        if self.hunger < 0 :
            self.hunger = 0
        self.__pass_time()

    #Снижает уровнь веселья животного
    def play(self, fun = 4):
        print('Ураа!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    pet_name = input('Как назавем свое животное:')
    pet = Pet(pet_name)
    choice = None
    while choice != '0':
        print(
            """
            Мой питомец
            0 - выйти
            1 - узнать о самочувствии
            2 - покормить животное
            3 - поиграть с животным
            """
        )
        choice = input("Ваш выбор: ")
        if choice == "0":
            print('До свидания!')
        elif choice == '1':
            pet.talk()
        elif choice == '2':
            pet.eat()
        elif choice == '3':
            pet.play()
        else:
            print('В меня нету такого значеия')

main()
input('Нажмите Enter для выхода')

