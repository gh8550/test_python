

# def add_many(*args):
#     result = 0
#     print(type(args))
#     print(args)
#     for i in args:
#         result = result + i
#     return result
# add_many(1,2,3,4,5)
#
#
#
# def add_and_mul(a,b):
#     return a+b, a*b
# a, m = add_and_mul(1,2)  #언팩킹
# print(a,m)
# print(add_and_mul(1,2))


# a = 1
# def vartest():
#     global c
#     c = a + 1
#     print(c)
# vartest()
# print(a)
# print(c)
# # print(c) 이건 안됨. 지역변수


# a = 1
# def vartest():
#     global a
#     a = 2
# vartest()
# print(a)


# def s(a):
#     print(a)
#
# s("python")

# def print_with_smile(a):
#     print(a + ':D')
#
# print_with_smile("python")


# def print_with_smile(*say):
#     for s in say:
#         print(s, end=' ')
#     print(':D')
#
# print_with_smile('안녕하세요~','오찬해 입니다~')
#
#


# number = int(input("숫자를 입력하세요: "))
# print(number)



'''
def add(a,b):
    return a+b
print(add(1,2))


def say():
    return 'Hi'
print(say())


# def add(a,b):
#     return "%d, %d의 합은 %d 입니다." %(a,b,a+b)
# print(add(1,2))


# def add(a,b):
#     print("%d, %d의 합은 %d 입니다." %(a,b,a+b))
# c =add(1,2)
# print(c)

def say():
    print('Hi')
print(say())'''

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result
# print(add_many(1,2,3,4,5,6))

# def add_mul(choice, *args):
#     if choice == 'add':
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result
# print(add_mul('mul', 1,2,3,4))


# def kwargs(**abc):
#     print(abc)
# kwargs(a=1, name= 'junho')
#
# def add_and_mul(a,b):
#     return a+b, a*b
#
# result1, result2 = add_and_mul(3,4)
# print(result1, result2)



# a = 1
# def vartest(a):
#     a = a +1
#     return a
#
# print(a)
# print(vartest(a))


# for i in range(10):
#     print(i, end='  ')


# f = open("새파일.txt", 'w')
# f.close()

