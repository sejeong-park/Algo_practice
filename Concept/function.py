# def 함수명(매개변수):
#   실행할 소스코드
#   return 반환 값

#ex1
def add(a,b):
    return a+b
print(add(3,7))

#ex2 : return문 없는 코드
def add(a,b):
    print("함수의 결과: ",a+b)
add(3,7)

#ex3 : a와 b(매개 변수)값을 지정해주면 매개변수의 순서가 달라져도 상관없다
def add(a,b):
    print('함수의 결과: ',a+b)
add(b=5,a=7)

#ex4 : 함수 안에서 함수 밖의 변수 데이터를 변경하는 경우 => global
#지역 변수를 만들지 않고 함수 바깥에 선언된 변수를 바로 참조
a=0
def func():
    global a
    a+=1

for i in range(10):
    func()
print(a)


#ex5 : 람다 표현식=> 함수를 매우 간단하게 작성하여 적용
#특정 기능을 수행하는 함수를 한 줄에 작성 가능
print((lambda a,b:a+b)(10,23))
#함수의 식을 람다로만 구현 가능한 메소드
#같은 식
def add(a,b):
    return a+b
print(add(10,23))

