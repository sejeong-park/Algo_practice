#홀수

#홀수만 저장될 리스트
odd=[]

#첫번째부터 일곱번째까지 자연수 입력
for i in range(0,7):
    num=int(input())

    #입력된 자연수가 홀수라면
    if num%2==1:
        odd.append(num)

#만약 홀수를 입력하지 않았다면
if len(odd)==0:
    print(-1)
#홀수가 있다면
else:
    #홀수의 합
    print(sum(odd))
    #최솟값
    print(min(odd))