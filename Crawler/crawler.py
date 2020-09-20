f = open("C:/Users/gh855/OneDrive/바탕 화면/Git/test_python/Crawler/Crawler_기초_HTML_예제.html", 'r', encoding='utf-8')
lines = f.readlines()
print(lines)

for i in lines:
    if "p" in i:
        print(i)
    f.close()