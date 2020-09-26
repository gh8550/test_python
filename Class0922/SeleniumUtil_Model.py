from selenium import webdriver
import time
# import calendar
# import datetime
#
# todayYear = datetime.datetime.now().year
# todayMonth = datetime.datetime.now().month
# endDay = calendar.monthrange(todayYear, todayMonth)[1]  #todayYear 변수를 빼버리면 함수가 작동하지 않음.
# print(todayYear)
# print(todayMonth)
# print(endDay)

class Selenium:
    def getDriver(self):
        self.driver = webdriver.Chrome('C:\chromedriver_win32/chromedriver.exe')
        self.driver.implicitly_wait(3)      #지연시간

    def linker(self, url):
        self.driver.get(url)
        print('linker')

    def clicker(self, xpath):
        button = self.driver.find_element_by_xpath(xpath)
        button.click()
        print('clicker')

    def scraper(self):
        print('scraper')

    def exit_(self):
        self.driver.close()
