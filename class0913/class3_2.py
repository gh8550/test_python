from class0913 import class3

class MoreFourCal(class3.FourCal):
    def add(self):
        result = (self.first * 2) + (self.second * 2)
        return result

    def pow(self):
        result = self.first ** self.second
        return result

def p():
    print('프린트할게염~')