#조건문이 참일 때 한해서, 반복해서 코드 수행

i=1
result=0

#i가 9보다 작거나 같을 때 코드 반복적으로 실행
while i<=9:
    result+=i
    i+=1

print(result)

#1부터 9까지 수 중 홀수만 더할 때,
i=1
result=0

while i<=9:
    if i%2==1:
        result+=i
    i+=1
print(result)