#1이 될 때까지
#N에서 1을 뺀다, K로 나눈다.
#N과 K가 주어질 때  N이 1이 될때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램

N,K=map(int,input().split())
count=0

# N이 K이상이라면  K로 나누기
while N>=K:
    while N%K!=0: #N이 K로 나누어 떨어지지 않는 다면 N에서 1씩 빼기
        N-=1
        count+=1
    #K로 나누기
    N//=K
    count+=1

#마지막 남은 수에 대한여 1씩 빼기
while N>1:
    N-=1
    count+=1
print(count)

