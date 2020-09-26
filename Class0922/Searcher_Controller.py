from Class0922.SeleniumUtil_Model import Selenium
import datetime
import calendar

class Searcher:
    def __init__(self):
        print('searcher')

    def judgeDateRange(self):
        print("한달을 꼬박 크롤링")
        print("원하는 날짜대로 크롤링")
        self.year = int(input('연도를 입력해주세요 : ') or datetime.datetime.now().year)
        self.month = int(input('월을 입력해주세요 : ') or datetime.datetime.now().month)
        self.day = int(input('일을 입력해주세요 : ') or 0)
        print(self.year)

    def getURL(self, url):
        print("url")
        year = str(self.year)
        month = '%02d' %self.month
        if self.day != 0:
            day = '%02d' %self.day
            self.url = url+year+month+day
        else:
            self.url = url + year + month

    def working(self):
        print('working')
        self.seleUtil = Selenium()
        self.seleUtil.getDriver()
        if self.day == 0:
            self.day = calendar.monthrange(self.year, self.month)[1]
            for day in range(1, self.day+1):
                self.seleUtil.linker(self.url + '%02d' %day)
                for i in range(1,31):
                    self.seleUtil.linker(self.url+ '%02d' %day)
                    self.seleUtil.clicker(
                        '//*[@id="wrap"]/table/tbody/tr/td[2]/div/div[4]/ol/li[%d]/div[2]/div[1]/a' % i)
                    self.seleUtil.scraper()

        for i in range(1,31):
            self.seleUtil.linker(self.url)
            self.seleUtil.clicker('//*[@id="wrap"]/table/tbody/tr/td[2]/div/div[4]/ol/li[%d]/div[2]/div[1]/a' %i)
            self.seleUtil.scraper()

        self.seleUtil.exit_()