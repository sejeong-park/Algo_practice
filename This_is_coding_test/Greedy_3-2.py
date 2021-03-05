#큰 수의 법칙
#N=배열의 크기
#M=숫자가 더해지는 횟수
#K=자연수

N,M,K=map(int,input().split())
#N개의 숫자를 공백으로 입력받기
data=list(map(int,input().split()))

data.sort()
first=data[N-1]#가장 큰 수
second=data[N-2]#두번째로 큰 수

result=0
while True:
    for i in range(K): #가장 큰 수를 K번 더하기
        if M==0: #M==0이 되면 반복문 탈출
            break
        result+=first#
        M-=1 #더할 때마다 1씩 빼기
    if M==0:
        break
    result+=second
    M-=1 #더할 때 마다 1씩 빼기

print(result)