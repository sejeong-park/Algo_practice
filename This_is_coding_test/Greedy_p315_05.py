#볼링공 고르기
#N은 볼링공의 개수,M은 볼링공의 무게 MAX
N,M=map(int,input().split())
weight=list(map(int,input().split()))
count=0

for i in range(len(weight)-1):
    for j in range(i+1,len(weight)):
        if weight[i]==weight[j]:
            continue
        count+=1

print(count)

