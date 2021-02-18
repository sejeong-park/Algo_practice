x=15
if x>=10:
    print(x)


#if~elif~else문
# if 조건문 1:
#   조건문 1이 True일 때 실행되는 코드
# elif 조건문 2:
#   조건문 1에 해당하지 않고, 조건문 2가 True일 때 실행되는 코드
# else:
#   위의 모든 조건문이 모두 True값이 아닐 때 실행되는 코드

score=85
if score>=70:
    print('성적이 70점 이상입니다.')
    if score>=90:
        print('우수한 성적입니다.')

else:
    print('성적이 70점 미만입니다.')
    print('조금 더 분발하세요')

print('프로그램을 종료합니다')

