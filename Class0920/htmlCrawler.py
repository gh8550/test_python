f = open("C:/Users/gh855/OneDrive/바탕 화면/Git/test_python/Crawler/Crawler_기초_HTML_예제.html", 'r', encoding='utf-8')
lines = f.readlines()
tag = False

# for i in lines:
#     if i.strip() == '</p>':
#         tag = False
#     if tag:
#         print(i.strip())
#     if i.strip() == '<p>':
#         tag = True

for i in lines:
    if i.strip() == '</title>':
        tag = False
    if tag:
        print(i.strip())
    if i.strip() == '<title>':
        tag = True

for i in lines:
    if i.strip() == '</h1>':
        tag = False
    if tag:
        print(i.strip())
    if i.strip() == '<h1>':
        tag = True

f.close()