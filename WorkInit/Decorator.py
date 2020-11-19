# generator list
# new_list = [i for i in range(1,21)]
# print(new_list)
#
# new_list2 = []
# for i in range(1,21):
#     new_list2.append(i)
# print(new_list2)

# list_ = [num for num in range(1,21) if num %2 == 0]
# print(list_)

# list_ = [num for num in range(1,21) if num %2 == 1]
# print(list_)

# lambda
# lambda_a = lambda  x ,y : x * y
# print(lambda_a (9,5))
# print(lambda_a (123,343))

# map
# list1 = ['1','2','3','4','5','6','7','8']
# list2 = list(map(int,list1))
# print(list2)

# li = [x for x in range(1,51)]
# def fun(x):
#     return x * x
# new_li = list(map(fun,li))
# print(new_li)

# list1 = [1,2,3,4,5,6,7,8,9]
#
# def my(element):
#     element = str(element) + 'element'
#     return element
#
# ine = map(my,list1)
# print(ine)

# Фильтр
# a = ['мак',"просо","мак","мак","просо","просо","мак"]
# b = list(filter(lambda x:x=="мак",a))
# print(b)


# def fil (num):
#     if (num % 2) == 0:
#         return True
#     else:
#         return False
# nums =  [1,2,3,4,5,6,7,8,9]
# output_fil = filter(fil,nums)
# print(tuple(output_fil))


# from functools import reduce
# num = [1,2,3,4,5]
# allnum = reduce(lambda x ,y: x + y,num )
# print(allnum)
#
# def lamda (x,y):
#     return x + y
# num2 = reduce(lamda, num)
# print(num2)

# zip

# a = [1,2,3,4]
# b = 'Hello'
# c = (None,True,False)
# res = list(zip(a,b,c))
# print(res)

# names = ['erkin', 'akylbek', 'islam']
# age = [ 31, 15, 15]
# tell = [123 , 123 ,123]
#
# new = dict(zip(names,age))
# new2 = list(zip(names,age,tell))
# new3 = set(zip(names,age,tell))
# new4 = tuple(zip(names,age,tell))
#
# print(new)
# print(new2)
# print(new3)
# print(new4)
#
# new[0] = 'nurbek'
# new['erkin'] = 'nurbek'
# print(new)

# функции енумкрт
# list_ = [1,1,2,3,4,5,6,7,8,9]
# new_list = []
# for nums in enumerate(list_):
#     new_list.append(nums)
# print(new_list)

# t = 'Hello world'
# for i in enumerate(t):
#     print(i)

# декоратор
# def hello ():
#     def hi():
#         print('hello')
#     hi()
# hello()
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

