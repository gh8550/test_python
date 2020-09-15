#2020.09.08.
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


#202009
# f = open("준호.txt", 'w', encoding='utf-8')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("준호.txt", 'r',encoding='utf-8')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()


#202009
# class cookieBox: # 과자 틀
#     def __init__(self, name): #생성자, 초기화 함수
#         print(name, '과자가 만들어 졌습니다.')
#
#     def a(self):
#         print('알러지를 유발합니다.')
#
#     def r(self, n):
#         print(n, '가 들어갑니다')
#
#
# if __name__=='__main__':
#     snack = cookieBox('치토스') # 생성한다!! /찍어냈다!!
#     snack.r('밀가루') # 밀가루가 들어갔다!!
#     snack.a()
#
#     s = cookieBox('새우깡')
#     snack.r('새우')
#
#     p = cookieBox('포스틱')
#     snack.r('감자')



# class OperationTest:
#     a = 1
#     b = 2
#
#     def __init__(self):
#         self.a = a
#         print('계산기를 호출하였습니다.')
#
#     def add(self):
#         print()
#
#     def multi(self):
#
# if __name__=='__main__':


# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result
#
# if __name__=='__main__':
#     cal = FourCal()
#     cal.setdata(3,4)
#     print(cal.div())

#2020.09.15.
# a = FourCal()
# a.setdata(4,2)
# print(a.add())

# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#
#
# a = FourCal()
# b = FourCal()
#
# a.setdata(4,2)
# print(a.first)
#
# b.setdata(3,7)
# print(b.first)
# print(a.first)

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,8)

print(a.add())
print(b.sub())



