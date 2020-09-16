class Book:
    def register(self):
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

    def select(self):
        book_name = input("책 이름을 입력하세요 :")
        f = open("서재.txt", 'r', encoding='utf-8')
        line = f.readline()
        if book_name in line:
            print("책이름: ", line[0])
            print("코드: ", line[-4:])
            f.close()
        else:
            print("책이 없습니다. 책을 등록해주세요")