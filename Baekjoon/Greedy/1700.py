#멀티탭 스케줄링
####실패
###모르겠음!!

N,K=map(int,input().split())
kind=list(map(int,input().split()))
plug=[]
cnt=0

for i in range(K):
    if kind[i] in plug:
        continue
    if len(plug)<N:
        plug.append(kind[i])
        continue

    idex=[]
    for j in range(N):
        try: