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

# def resister:
#     print("책 이름을 적어주세요")


x = '''------------------------
1. 종료
2. 선택
3. 등록
------------------------'''


while True:
    print(x)
    number = input("1~3 사이의 숫자를 입력하세요: ")

    # 3.등록
    if number =='3':
        book_name = input("책 이름을 입력하세요 :")
        book_code = int(input("코드를 입력하세요 :"))

        f = open("서재.txt", 'w', encoding='utf-8')
        book = "%s : %d" % (book_name, book_code)
        f.write(book)
        f.close()
        print('*' * 20)
        print("책이 입력 되었습니다.")
        print("->", book)
        print('*' * 20)

    # 2. 선택
    elif number == '2':
        book_name = input("책 이름을 입력하세요 :")
        f = open("서재.txt", 'r', encoding='utf-8')
        line = f.readline()
        if book_name in line:
            print("책이름: ", line[0])
            print("코드: ", line[-4:])
            f.close()
        else:
            print("책이 없습니다. 책을 등록해주세요")

    # 1.종료
    if number == '1':
        print("프로그램을 종료합니다.")
        break