
##비교 연산자
#X==Y : X와 Y가 서로 같을 때 참이다
#X!=Y : X와 Y가 서로 다를 때 참이다
#X>Y
#X<Y
#X>=Y
#X<=Y

##논리 연산자
#X and Y : X와 Y가 모두 참일 때 참이다
#X or Y : X와 Y 중에 하나만 참이어도 참이다
#not X : X가 거짓일 때 참이다

##in 연산자
#X in 리스트 : 리스트 안에 X가 들어가 있을 때 참이다
#X not in 문자열 : 문자열 안에 X가 들어가 있지 않을 때 참이다

score=85
if score>=80:
    pass
else:
    print('성적이 80점 미만입니다.')
print('프로그램을 종료합니다')


score=85
if score>=80:
    result="Success"
else:
    result="Fail"

score=85
result="Success" if score>=80 else "Fail"
print(result)
