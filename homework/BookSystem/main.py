from Homework.BookSystem.Book import Book
if __name__=="__main__":
    b = Book()
    def menuUI():
        print('-'*30)
        print('1. 종료')
        print('2. 선택')
        print('3. 등록')
        print('-' * 30)

    def selectMenu():
        temp = int(input('입력하세요. :'))
        return temp

    while True:
        menuUI()
        number = selectMenu()

        # 3.등록
        if number == 3:
            b.register()

        # 2. 선택
        elif number == 2:
            b.select()