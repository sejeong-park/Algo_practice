#숫자의 개수

a=int(input())
b=int(input())
c=int(input())
#a*b*c의 값을 문자열 str로 변환하고 변환 값을 list에 넣어준다
result=list(str(a*b*c))
#list에 그 문자가 몇개씩 있는지 프린트해준다
for i in range(10):
    print(result.count(str(i)))