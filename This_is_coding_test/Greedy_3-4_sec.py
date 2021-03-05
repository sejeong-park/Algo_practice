N,K=map(int,input().split())
count=0

while True:
    #(N==K로 나누어떨어지는 수)가 될때까지 1씩 빼기
    target=(N//K)*K
    count+=(N-target)
    N=target
    #N이 K보다 작을때(더 이상 작은 수가 없을 때) 반복문 탈출
    if N<K:
        break
    #K로 나누기
    count+=1
    N//=K
#마지막으로 남은 수에 대하여 1씩 빼기
count+=(N-1)
print(count)