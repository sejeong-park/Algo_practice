#뒤집기

data=input()

cnt=0 #변곡점을 카운트
for i in range(len(data)-1):
    if data[i]!=data[i+1]:
        cnt+=1

print((cnt+1)//2)