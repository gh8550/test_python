f = open("Crawler 기초 HTML 예제.html", 'r', encoding='utf-8')
lines = f.readlines()
for i in lines:
    print(i.attrs['p'])
    f.close()