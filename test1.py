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

#선생님 방식ㅇ로 한번해보기
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


score = [x for x in range(0,101,10)]
print(score)