#001~010
# print("Hello World")
#
# print("Mary's cosmetics")
#
# print('신씨가 소리질렀다. "도둑이야".')
#
# print('"c:\Windows"')
#
# print("안녕하세요. \n만나서\t\t반갑습니다.")
#
# print("오늘은","일요일")
#
# print("naver;kakao;sk;samsung")
# print("naver","kakao",'sk', 'samsung', sep=';')
# print("naver","kakao",'sk', 'samsung', sep='/')
#
# print("first");print("second")
# print("first",end=""); print("second")
#
# a = 5/3
# print(a)
# print(5/3)

#011~012
# #011
# 삼성전자= 50000
# 총평가금액 = 삼성전자*10
# print(총평가금액)
#
# #012
# 시가총액=2980000000000
# 현재가= 50000
# PER=15.79
# print(시가총액, type(시가총액))
# print(현재가, type(현재가))
# print(PER, type(PER))
#
# #013
# s = "hello"
# t = "python"
# print(s+"! "+t)
# print(s,"!",t)
#
# #015
# a = "132"
# print(type(a))
#
# #016
# num_str = "720"
# print(int(num_str))
#
# #017
# num = 100
# num_str= str(num)
# print(num_str, type(num_str))
#
# #018
# a= "15.79"
# b= float(a)
# print(b, type(b))
#
# #019
# year = "2020"
# a= int(year)
# print(a,a-1, a-2)
#
# #020
# month_cost = 48584
# total_cost = month_cost * 36
# print(total_cost, type(total_cost))

#021~030
# letters = 'python'
# print(letters[0],letters[2])
#
# license_plate = "24가 2210"
# print(license_plate[-4:])
#
# string= "홀짝홀짝홀짝"
# print(string[0],string[2],string[4])
# print(string[::2])
#
# string = "PYTHON"
# print(string[::-1])
#
# phone_number = "010-1111-2222"
# print(phone_number.replace('-',' '))
# print(phone_number)
#
# print(phone_number.replace('-',' '))
# phone_number1= phone_number.replace('-',' ')
# print(phone_number1)
#
# url = "http://sharebook.kr"
# print(url[-2:])
# url_split = url.split('.')
# print(url_split)
# print(url_split[-1])
#
# # lang = 'python'
# # lang[0]='P'
# # print(lang)
# #아마도 에러 나올듯. 왜냐하면 문자열 자료형은 수정할수없는 자료형이라서
#
# string = 'abcdfe2a354a32a'
# a= string.replace('a', 'A')
# print(a)
#
# #abcd 맞춤 ㅇㅇ

#031~040
# #34
# #HiHiHi
# print('-'*80)
#
# t1 = 'python'
# t2 = 'java'
# t3 = t1+' '+t2 +' '
# print(t3*4)
#
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
#
# print("이름: %s 나이: %d" %(name1, age1))
# print("이름: %s 나이: %d" %(name2, age2))
#
# print("이름: {0} 나이: {1}".format(name1,age1))
# print("이름: {0} 나이: {1}".format(name2,age2))
#
# print("이름: {name3} 나이: {age3}".format(name3="장준호",age3=26))
# print("이름: {name4} 나이: {age4}".format(name4="nathan",age4=24))
#
# print("이름: {} 나이: {}".format(name1,age1))
# print("이름: {} 나이: {}".format(name2,age2))
#
# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")
#
# 상장주식수 = "5,969,782,550"
# b = 상장주식수.replace(',','')
# print(b)
#
# 타입변환 = int(b)
# print(타입변환, type(타입변환))
#
#
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])
#
# data = "   삼성전자    "
# print(data.strip())
# data1 = data.strip()
# print(data1)

#041~050
# ticker = "btc_krw"
# ticker1 = ticker.upper()
# print(ticker1)
# print(ticker.upper())
#
# ticker = "BTC_KRW"
# ticker1 = ticker.lower()
# print(ticker1)
#
# a = 'hello'
# print(a.capitalize())
#
# file_name="보고서.xlsx"
# print(file_name.endswith('xlsx'))
# print(file_name.endswith(('xlsx', 'xls')))
#
# file_name = "2020_보고서.xlsx"
# print(file_name.startswith('2020'))
#
# a = "hello world"
# b= a.split()
# print(b)
#
# ticker = "btc_krw"
# print(ticker.split('_'))
#
# date = "2020-05-01"
# print(date.split('-'))
#
# data = "039490     "
# print(data.rstrip())
# print(data)

#051~060
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# movie1 = ["배트맨"]
# print(movie_rank + movie1)
#
# # print(movie_rank.append('배트맨'))
# # print(movie_rank.insert(3, '배트맨'))
# movie_rank.append('배트맨')
# print(movie_rank)
#
# movie_rank.insert(2,'배트맨')
# print(movie_rank)
#
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1,"슈퍼맨")
# print(movie_rank)
#
# movie_rank.remove('럭키')
# print(movie_rank)
#
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2:]
# print(movie_rank)
#
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 + lang2
# print(langs)
#
# nums = [1, 2, 3, 4, 5, 6, 7]
# print("max: ", max(nums))
# print("min: ", min(nums))
#
# nums = [1, 2, 3, 4, 5]
# nums_sum= nums[0]+nums[1]+nums[2]+nums[3]+nums[4]
# print(nums_sum)
#
# print(sum(nums))
#
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# print(len(cook))
#
# nums = [1, 2, 3, 4, 5]
# average= sum(nums)/len(nums)
# print(average)

#061~070
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])
# print(nums[1::2])
#
# nums = [1, 2, 3, 4, 5]
# nums.reverse()
# print(nums)
#
# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])
#
# interest = ['삼성전자', 'LG전자', 'Naver']
# interest.pop(1)
# print(''.join(interest))
#
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(' '.join(interest))
#
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print('/'.join(interest))
#
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print('\n'.join(interest))
#
# string = "삼성전자/LG전자/Naver"
# print(string.split('/'))
#
# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)

#071~080
# my_variable = ()
# print(type(my_variable))
#
# movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
#
# a = (1,)
# print(type(a))
#
# t = 1,2,3,4
# print(type(t))
#
# t = ('a', 'b', 'c')
# a = ('A',)
# print(a+t[1:])
#
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# # print(interest.split())
# data = list(interest)
# print(data)
#
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# data = tuple(interest)
# print(data)
#
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
#
# a = range(2,100,2)
# print(tuple(a))

#084
# temp={}
#
# #085
# a= {'메로나':1000, '폴라포':1200, '빵빠레':1800}
# print(a)
#
# #086
# a['죠스바']=1200
# a['월드콘']=1500
# print(a)
#
# #087
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# print('메로나 가격:', ice.get('메로나'))
#
# #088
# ice['메로나'] = 1300
# print(ice)
#
# #089
# del ice['메로나']
# print(ice)

#91~100
# #090
# key 중에 누가바가 없기 때문!! 만약 에러대신 none으로 나오게 하고싶으면
# icecream.get('누가바')를 사용하면 됨.

# #091
# inventory = {'메로나':[300,20],
#              '비비빅':[400,3],
#              '죠스바':[250,100]}
# print(inventory)
#
# #092
# print(inventory['메로나'][0],'원')
#
# #093
# print(inventory['메로나'][1],'개')
#
# #094
# inventory['월드콘']=[500,7]
# print(inventory)
#
# #095
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# a = list(icecream.keys())
# print(a)
#
# #096
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# price = list(icecream.values())
# print(price)
#
# #097
# print(sum(price))
#
# #098
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# # icecream=icecream+new_product
# # print(icecream)
# icecream.update(new_product)
# print(icecream)
#
# #099
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = dict(zip(keys,vals))
# print(result)
#
# #100
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# close_table = dict(zip(date,close_price))
# print(close_table)

#101~110
#101
#bool 타입

#102
#False

#103
#True

#104
#True

#105
#True

#106
#'>='라고 써야함

#107
#아무결과도 출력되지 않음

#108
#Hi, there.

#109
#1
#2
#4

#110
#3
#5

#111~120
#111
# user = input("입력:")
# print(user*2)

#112
# user = int(input("숫자를 입력하세요: "))
# print(user+10)

#113
# num = int(input())
# if num%2 == 0:
#     print('짝수')
# else:
#     print("홀수")

#114
# user = input("입력값: ")
# if int(user) +20 <= 255:
#     print("출력값:", int(user)+20)
# else:
#     print("출력값::", 255)

# user = input("입력값: ")
# num = 20 +int(user)
# if num>255:
#     print("출력값:",255)
# else:
#     print("출력값:",num)

#115
# user=input("입력값: ")
# num= int(user)-20
# if num<0:
#     print("출력값:",0)
# elif num>255:
#     print("출력값:",255)
# else:
#     print("출력값:",num)

#116
# user = input('현재시간:')
# if int(user[3:]) == 00:
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")

#117
# fruit = ["사과", "포도", "홍시"]
# user = input("좋아하는 과일은?")
# if user in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

#118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# 종목 = input("투자종목을 작성해주세요 \n")
# if 종목 in warn_investment_list:
#     print("투자 경고 종목입니다")
# else:
#     print("투자 경고 종목이 아닙니다.")

#119
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("제가 좋아하는 계절은:")
# if user in fruit:
#     print("정답입니다.")
# else:
#     print(("오답입니다."))

#120
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("좋아하는 과일은:")
# if user in fruit.values():
#     print("정답입니다.")
# else:
#     print(("오답입니다."))

#121~130
#121
# user = input()
# if user.islower() ==True:
#     print(user.upper())
# else:
#     print(user.lower())

#122
# score = int(input("학점을 입력하시오 \n"))
# if score<=100 and score > 80:
#     print("A")
# elif score > 60 and score <=80:
#     print("B")
# elif score > 40 and score <=60:
#     print("C")
# elif score > 20 and score <=40:
#     print("D")
# else:
#     print("E")

# score = input("학점을 입력하시오. \n")
# score = int(score)
# if 81 <=score <= 100:
#     print("당신의 학점은 A입니다.")
# elif 61 <=score <= 80:
#     print("당신의 학점은 B입니다.")
# elif 41 <=score <= 60:
#     print("당신의 학점은 C입니다.")
# elif 21 <=score <= 40:
#     print("당신의 학점은 D입니다.")
# else:
#     print("당신의 학점은 E입니다.")

#123
# user = input("입력: ")
# if "달러" in user:
#     print(int(user[:-3])*1167, "원")
# elif "유로" in user:
#     print(int(user[:-3])*1268, "원")
# elif "위안" in user:
#     print(int(user[:-3])*171, "원")
# else:
#     print(int(user[:-2]) * 1.096, "원")

# 환율 = {"달러":1167,"엔":1.096,"유로":1268,"위안":171}
# user = input("입력: ")
# 앞, 뒤 = user.split()
# print(float(앞)*환율[뒤], '원')

#124
# user1 = int(input("input number1: "))
# user2 = int(input("input number1: "))
# user3 = int(input("input number1: "))
# if user1>user2 and user1>user3:
#     print(user1)
# elif user2>user1 and user2>user3:
#     print(user2)
# else:
#     print(user3)

#125
# user= input("휴대전화 번호 입력:")
# if user[:4] == '010':
#     print("당신은 SKT 사용자입니다.")
# elif user[:4] == '016':
#     print("당신은 KT 사용자입니다.")
# elif user[:4] == '019':
#     print("당신은 LGU 사용자입니다.")
# else:
#     print("당신은 누구세요?ㅋㅋ")

#126
# user = input("우편번호: ")

#131~140
#131
# 사과
# 귤
# 수박

#132
#####
#####
#####

#133
# print("A")
# print("B")
# print("C")
#
# 변수 = "A"
# print(변수)
# 변수 = "B"
# print(변수)
# 변수 = "C"
# print(변수)

#134
# print("출력:", "A")
# print("출력:", "B")
# print("출력:", "C")

#135
# 변수 = "A"
# b= 변수.lower()
# print("변환:", b)
# 변수 = "B"
# b= 변수.lower()
# print("변환:", b)
# 변수 = "C"
# b= 변수.lower()
# print("변환:", b)
#
# print("변환:", "a")
# print("변환:", "b")
# print("변환:", "c")

#136
# for 변수 in [10, 20, 30]:
#     print(변수)

#137
# for 변수 in [10, 20, 30]:
#     print(변수)

#138
# for 변수 in [10,20,30]:
#     print(변수)
#     print("-------")

#139
# print("++++")
# for 변수 in [10,20,30]:
#     print(변수)

#140
# for 변수 in [1,2,3,4]:
#     print("-------")

#141~150
# #141
# 리스트 = [100,200,300]
# for i in 리스트:
#     print(i+10)
#
# #142
# 리스트=["김밥","라면","튀김"]
# for 변수 in 리스트:
#     print("오늘의 메뉴:",변수)
#
# #143
# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# for 길이 in 리스트:
#     print(len(길이))
#
# #144
# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i,len(i))
#
# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i+str(len(i)))
#
# #145
# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i[0])
#
# #146
# 리스트 = [1,2,3]
# for i in 리스트:
#     print("3 x",i)
#
# #147
# 리스트=[1,2,3]
# for i in 리스트:
#     print("3 x",i,"=",3*i)
#     print("3 x {} = {}".format(i, 3*i))
#
# #148
# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[1:]:
#     print(i)
#
# #149
# 리스트 = ["가", "나", "다", "라"]
# 리스트 = 리스트[0] + 리스트[2]
# for i in 리스트:
#     print(i)
#
# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[::2]:
#     print(i)
#
# #150
# 리스트 = ["가", "나", "다", "라"]
# 리스트.reverse()
# for i in 리스트:
#     print(i)
#
# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[::-1]:
#     print(i)

#151~160
#151
# 리스트 = [3, -20, -3, 44]
# for i in 리스트:
#     if i <0:
#         print(i)

#152
# 리스트 = [3, 100, 23, 44]
# for i in 리스트:
#     if i%3 == 0:
#         print(i)

#153
# 리스트 = [13, 21, 12, 14, 30, 18]
# for i in 리스트:
#     if (i <20) and (i%3==0):
#         print(i)

#154
# 리스트 = ["I", "study", "python", "language", "!"]
# for i in 리스트:
#     if len(i) >= 3:
#         print(i)

#155
# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#     if i.isupper() == True:
#         print(i)

#156
# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#     if i.islower()==True:
#         print(i)
#
# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#     if i.isupper()!=True:
#         print(i)

#157
# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i.capitalize())

#158
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# for i in 리스트:
#     a = i.split('.')
#     print(a[0])

#159
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#     if '.h' in i:
#         print(i)

#160
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#     a = i.split('.')
#     if a[1] == 'h' or a[1] == 'c':
#         print(i)

#이렇게 해도됨! 다만 'h' or 'c' in i 이렇게 쓰면
# h를 True로 인식해서 결과값으로 run.py가 나오게 됨. 주의!!
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#     if 'h' in i or 'c' in i:
#         print(i)

#161~170
#161
# for i in range(0,100):
#     print(i)

#162
# for i in range(2002,2051,4):
#     print(i)

#163
# for i in range(1,31):
#     if i%3 == 0:
#         print(i)
#
# for i in range(3,31,3):
#     print(i)

#164
# for i in range(99,-1,-1):
#     print(i)
#
# for i in range(100):
#     print(99-i)

#165
# for i in range(10):
#     print('0.'+str(i))

# for num in range(10):
#     print(num / 10)

#166
# for i in range(1,10):
#     print(3,"x",i,'=',i*3)

#167
# for i in range(1,10):
#     if i%2==1:
#         print(3,"x",i,"=",3*i)

#168
# a = 0
# for i in range(1,11):
#     a = a + i
# print(a)

#169
# a = 0
# for i in range(1,11,2):
#     a += i
# print(a)

#170
# a=1
# for i in range(1,11):
#     a *= i
# print(a)

#171~180
#171
# price_list = [32100, 32150, 32000, 32500]
# for i in price_list:
#     print(i)

# for i in range(4):
#     print(price_list[i])

#172
# price_list = [32100, 32150, 32000, 32500]
# for i in range(4):
#     print(i, price_list[i])

#173
# price_list = [32100, 32150, 32000, 32500]
# for i in range(4):
#     print(3-i, price_list[i])
#
# for i in range(len(price_list)):
#     print((len(price_list)-1)-i, price_list[i])

#174
# price_list = [32100, 32150, 32000, 32500]
# for i in range(3):
#     print(100+i*10, price_list[i+1])

#175
# my_list = ["가", "나", "다", "라"]
# print(my_list[0:2])
# print(my_list[1:3])
# print(my_list[2:4])
# for i in range(3):
#     print(my_list[i:i+2])
#
# print(my_list[0],my_list[1])
# print(my_list[1],my_list[2])
# print(my_list[2],my_list[3])

# for i in range(len(my_list)-1):
#     print(my_list[i], my_list[i+1])

#176
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list)-2):
#     print(my_list[i], my_list[i+1], my_list[i+2])

# for i in range(2, len(my_list)):
#     print(my_list[i-2], my_list[i-1], my_list[i])

#177
# my_list = ["가", "나", "다", "라"]
# for i in range(1, len(my_list)):
#     print(my_list[4-i],my_list[3-i])

# print(my_list[3],my_list[2])
# print(my_list[2],my_list[1])
# print(my_list[1],my_list[0])

# for i in range(len(my_list)-1):
#     print(my_list[len(my_list)-1-i],my_list[len(my_list)-2-i])

#178
# my_list = [100, 200, 400, 800]
# for i in range(3):
#     print(my_list[i+1]-my_list[i])

#179
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(4):
#     print((my_list[i]+my_list[i+1]+my_list[i+2])/3)

#180
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility = []
# for i in range(5):
#     volatility.append(high_prices[i]-low_prices[i])
# print(volatility)

#181~190
#181
# apart =[["101호","102호"],["201호","202호"],["301호","302호"]]

#182
# stock=[["시가",100,200,300],["종가",80,210,330]]

#183
# stock={"시가":[100,200,300],"종가":[80,210,330]}

#184
# stock = {"10/10":[80,110,70,90], "10/11":[210,230,190,200]}

#185
# apart = [ [101, 102], [201, 202], [301, 302] ]
# print(apart[0][0],'호')

# for i in [0,1,2]:
#     print(apart[i][0],'호')
#     print(apart[i][1],'호')

# for floor in apart:
#     for ho in floor:
#         print(ho, "호")

# 186
# apart = [ [101, 102], [201, 202], [301, 302] ]
# apart.reverse()
# for floor in apart:
#     for ho in floor:
#         print(ho, "호")


