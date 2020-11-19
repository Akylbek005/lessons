# number 1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i <= 5:
#         print(i)
# list()

# number 2
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# b = [list for list in a if list in b ]
# print(b)

# number 3
# a = {'a':'1','b':2}
# b = {'c':'3','d':4}
# a.update(b)
# print(a)

# number 4
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
# 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687,217,]
#
# for i in numbers:
#     if (i % 2) == 0:
#         print(i)
#     elif i == 237:
#         break

# 5
# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
# c = b + 1
# res = [i for i in range(a,c)]
# print(res)

# 6***
# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
# c = [i ** 2 for i in range(a , b+1)]
# print(c)
#
# for i in c:
#     if i < c:
#         print(c)

# 7
# a = [1, 2, 6, 3, 9, 2, 11, 20, 16, 7, 8]
# for i in a:
#     if (i % 2) == 1:
#         print('\n'"Это не четное!")
#         print(i,)
#     elif (i % 2) == 0:
#         print('\n''Это четное')
#         print(i,)

# 8
# a = int(input('введите число:'))
# b = int(input('введите конечное число:'))
# for i in range(a,b):
#     for a in range(i):
#         print(i,end = '')
#     print('\n')

# 9
# a = 1
# b = 11
# for i in range(a,b):
#     c = i *2
#     print(f"2 * {i} = {c}")

# 10
# a = int(input('Введите первое число :'))
# b = int(input('Введите конечное число:'))
# c = int(input('Введите интервал:'))
# for i in range(a,b,c):
#     print(i)

# 11
# n = int(input('Число Фибоначи:'))
# a = 1
# b = 1
#
# print(a)
# print(b)
#
# for i in range(0, n-2):
#     a , b = b , a + b
#     print(b)

# 12
# a = int(input('Узнать факториал какого числа?:'))
# for i in range(1 , 12):
    # a = a * i
    # print(a)



