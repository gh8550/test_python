'''[91, 80, 72, 64, 59]

90이상 : 아주잘했어요
80이상 : 잘했어요
70이상 : 노력하세요
60이상 : 공부하세요
60미만 : 낙제


score = 91

if score >= 90:
    print("아주 잘했어요")
elif score >= 80:
    print("잘했어요")
elif score >= 70:
    print("노력하세요")
elif score >= 60:
    print("공부하세요")
else:
    print("낙제")


for i in range(2,6,2):
    print(i)



temp= [1,2,3,4,(5,6)]
for x in temp:
    print(x)


temp = [(1,2),(3,4),(5,6)]
# 언패킹
for a,b temp:
    print(a+b)
'''

# test = [91, 80, 72, 64, 59]
# for i, score in enumerate(test):
#     print(i+1,"번째 학생은 ", end='')
#     if score >= 90:
#         print("아주 잘했어요")
#     elif score >= 80:
#         print("잘했어요")
#     elif score >= 70:
#         print("노력하세요")
#     elif score >= 60:
#         print("공부하세요")
#     else:
#         print("낙제")

# # 선생님 방식ㅇ로 한번해보기
# test = [91, 80, 72, 64, 59]
# for i, score in enumerate(test):
#     if score >= 90:
#         print("아주 잘했어요")
#     elif score >= 80:
#         print("잘했어요")
#     elif score >= 70:
#         print("노력하세요")
#     elif score >= 60:
#         print("공부하세요")
#     else:
#         print("낙제")


# score = [x for x in range(0,101,10)]
# print(score)


# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit +1
#     print("나무를 %d번 찍었습니다." %treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다")
#
#
# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit
#
# Enter number"""
#
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())


# coffee= 10
# while True:
#     money = int(input("돈을 넣어주세요 : "))
#     if money == 300:
#         print("커피를 줍니다")
#         coffee = coffee - 1
#     elif money >300:
#         print("거스름돈 %d를 주고 커피를 줍니다." %(money-300))
#         coffee = coffee-1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다" %coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break



#Q1
# 결과값: shirt need


