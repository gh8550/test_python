class Resister:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

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