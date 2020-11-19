# 1
# def polindrom():
#     user = input('Слово:')
#     user1 = user[::-1]
#     if user == user1:
#         print('True')
#     else:
#         print('False')
# polindrom()

# 2 ***
# a = input('Введите слово:')
# print(a.index(''))
# print(a.rindex(''))

# 3
# def num (a ,b, c):
#     print(a + b + c)
# a = int(input(':'))
# c = int(input(':'))
# b = int(input(':'))
# num(a, b, c)


# 4
# user = input('Введите слово через пробел:')
# a = user.split()
# print(sorted(a, key = len))

# 5
# a = 'hello world'
# b = input()
# if b in a:
#     print('hello')
# else:
#     print('Bye')

# 6 ***
# list_ = [i for i in range(1500, 2701)]
# list2 = []
# for i in list_:
#     if i % 5 == 0 and i % 7 == 0:
#         list2.append(i)
# print(list2)


# 7
# for i in range(0,6):
#     i += 1
#     if i == 3 or i == 6:
#         continue
#     print(i)

# 8
# user1 = input('Введит слово:')
# a = user1.lower()
# if a == user1:
#     d = user1.upper()
#     print(f'Вы ввели {d}')
# else:
#     print('Введите слово в нижнем регистре!')

# 9 ***
# a = []
# b = []
#
# user = input('Введите слово:')
# for i in user:
#     if i.isdigit():
#         a.append(i)
#     elif i.isalpha():
#         b.append(i)
# print(a)
# print(b)


# 10
# user = input('Введите букву:')
# if len(user) > 1:
#     print('Введите одну букву')
# elif user in 'a,e,y,u,o':
#     print('Это гласный')
# else:
#     print('Это согласный')

# 11
# list1 = []
# while True:
#     user = input('Введите число:')
#     if user == 'end':
#         break
#     list1.append(user)
#
# a = list(map(int, list1))
# b = sum(a)
# print(a)
# print(b)
# print(b / len(a))


# 12
# name = input('Ваше имя:')
# last_name = input('Ваше фамилие:')
# years = int(input('В каком году вы родились:'))
# city = input('В каком городе вы живете:')
# years = 2020 - years
# print(f"Привет {last_name} {name}. Вам {years} лет. Вы живете в городе {city}.")

# 13
yoda = ['on Python','programming', 'I like']
a = yoda[0]
b = yoda[1]
c = yoda[2]
a, b ,c = c, b, a
print(a , b , c)

# 14









