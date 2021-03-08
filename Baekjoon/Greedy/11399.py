#ATM

N=int(input())
P=list(map(int,input().split()))

P.sort()

index_sum=0#이전 사람들이 돈을 인출하는데 걸리는 시간
min_sum=0

for i in range(N):
    min_sum+=(index_sum+P[i])
    index_sum+=P[i]

print(min_sum)