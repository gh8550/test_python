# 내가 처음에 한거!
# x = '''------------------------
# 1. 종료
# 2. 선택
# 3. 등록
# ------------------------'''
#
#
# while True:
#     print(x)
#     number = input("1~3 사이의 숫자를 입력하세요: ")
#
#     # 3.등록
#     if number =='3':
#         book_name = input("책 이름을 입력하세요 :")
#         book_code = int(input("코드를 입력하세요 :"))
#
#         f = open("서재.txt", 'w', encoding='utf-8')
#         book = "%s : %d" % (book_name, book_code)
#         f.write(book)
#         f.close()
#         print('*' * 20)
#         print("책이 입력 되었습니다.")
#         print("->", book)
#         print('*' * 20)
#
#     # 2. 선택
#     elif number == '2':
#         book_name = input("책 이름을 입력하세요 :")
#         f = open("서재.txt", 'r', encoding='utf-8')
#         line = f.readline()
#         if book_name in line:
#             print("책이름: ", line[0])
#             print("코드: ", line[-4:])
#             f.close()
#         else:
#             print("책이 없습니다. 책을 등록해주세요")
#
#     # 1.종료
#     if number == '1':
#         print("프로그램을 종료합니다.")
#         break




# import sys
#
# def menuUI():
#     print('-'*30)
#     print('1. 종료')
#     print('2. 선택')
#     print('3. 등록')
#     print('-' * 30)
#
# def selectMenu():
#     temp = int(input('입력하세요. :'))
#     return temp
#
# def resisterBook():
#     book_name = input("책 이름을 입력하세요 :")
#     book_code = int(input("코드를 입력하세요 :"))
#
#     f = open("서재.txt", 'w', encoding='utf-8')
#     book = "%s : %d" % (book_name, book_code)
#     f.write(book)
#     f.close()
#     print('*' * 20)
#     print("책이 입력 되었습니다.")
#     print("->", book)
#     print('*' * 20)
#
# def exitProgram():
#     print("프로그램을 종료합니다.")
#     sys.exit()
#
# def selectBook():
#     book_name = input("책 이름을 입력하세요 :")
#     f = open("서재.txt", 'r', encoding='utf-8')
#     line = f.readline()
#     if book_name in line:
#         print("책이름: ", line[0])
#         print("코드: ", line[-4:])
#         f.close()
#     else:
#         print("책이 없습니다. 책을 등록해주세요")
#
# if __name__=='__main__':
#     while True:
#         menuUI()
#         number = selectMenu()
#
#         # 3.등록
#         if number == 3:
#             resisterBook()
#
#         # 2. 선택
#         elif number == 2:
#             selectBook()
#
#         # 1.종료
#         if number == 1:
#             exitProgram()




# def inputData():
#     a = int(input())
#     b = int(input())
#     return a, b
#
# def print_arithmetic_operation(a,b):
#     print('%d + %d =' % (a,b), a+b)
#     print('%d - %d =' % (a,b), a-b)
#     print('%d * %d =' % (a,b), a*b)
#     print('%d / %d =' % (a,b), a/b)
#
# if __name__=='__main__':
#     c,d = inputData()
#     print_arithmetic_operation(c,d)





