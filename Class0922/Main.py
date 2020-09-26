from Class0922.Searcher_Controller import Searcher

if __name__=='__main__':
    print('main')
    a = Searcher()
    a.judgeDateRange()
    a.getURL('https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=105&date=')
    a.working()