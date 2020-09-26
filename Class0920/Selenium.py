from selenium import webdriver
import time
import calendar
import datetime

todayYear = datetime.datetime.now().year
todayMonth = datetime.datetime.now().month
endDay = calendar.monthrange(todayYear, todayMonth)[1]

class Selenium:
    link = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=105&date=202009'
    # link2 = '//*[@id="wrap"]/table/tbody/tr/td[2]/div/div[4]/ol/li[%d]/div[2]/div[1]/a'

    def __init__(self):
        self.driver = webdriver.Chrome('C:\chromedriver_win32/chromedriver.exe')
        self.driver.implicitly_wait(3)      #지연시간

    def linkUrl(self):
        for i in range(1,endDay):
            day = '%02d' %i     #%02d 하면 1은 01로 표현, %03d하면 1은 001로 표현
            self.driver.get(self.link + day)
            time.sleep(3)
            self.searcher(day)

    def searcher(self, day):
        for i in range(1,31):
            button = self.driver.find_element_by_xpath('//*[@id="wrap"]/table/tbody/tr/td[2]/div/div[4]/ol/li[%d]/div[2]/div[1]/a' %i)
            button.click()
            time.sleep(2)

            self.driver.get(self.link + day)
            time.sleep(2)

    def exit_(self):
        self.driver.close()

if __name__ == '__main__':
    a = Selenium()
    a.linkUrl()
    a.searcher(day)
    a.exit_()


