#게임을 만든 동준이
N=int(input())
data=[]
for i in range(N):
    data.append(int(input()))
cnt=0
for i in range(N-1,0,-1):#3부터 0까지 -1간격으로 포문
    if data[i]<=data[i-1]:
        cnt+=(data[i-1]-data[i]+1)
        data[i-1]=data[i]-1

print(cnt)

