#홀짝 구분
temp = 21379
if temp%2 == 0:
    print(temp, '는 짝수입니다.')
else:
    print(temp, '는 홀수입니다.')



def f(temp):
    if temp %2 == 0:
        return '짝수'
    else:
        return '홀수'
temp = 7
print(f(temp))

