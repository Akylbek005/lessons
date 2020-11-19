# def add(q, w, e,r ,t, y, i,o,p ):
#     return q + w + e + r + t + y + i + o + p
# print(add(1,2,3,4,5,6,7,8,9))

# def add (*num):
#     result = 0
#     for nums in num:
#         result = result + nums
#     return result
#
# print(add(1,2,3,4,5,6,7,8,9))

# def fun(a = 10, b = 20,c = 30 ):
#     return a + b + c
# print(fun(10,22))

# fun =  dict(Myname = "Akyl",a = "calam",b = "Hello")
#     # print(f"{Myname},\n{a}\n{b}")
# # fun(a  = "Privet")
#
# def fun2 (**kwargs):
#     for key, value in fun.items():
#         print(f"{key}:{value}")
#fun2()

# def a():
#     print("Всем привет")
#     a()
# a()

def fac(n):
    if n == 0:
        return 1
    else:
        print(f"{n} * fac({n} - 1)")
        return n * fac(n-1)
print(fac(5))