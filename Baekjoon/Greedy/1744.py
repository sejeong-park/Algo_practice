#수 묶기

N=int(input())
data=[]
for i in range(N):
    data.append(int(input()))

#0을 포함한 음수는 작은 수 부터 묶는다.
#1보다 큰 수는 큰 수부터 묶는다
#숫자가 1인 경우에는 묶지 않는다

neg=[]
pos=[]
ans=0

for num in data:
    if num<=0: #0도 neg로 둔다
        neg.append(num)
    elif num==1:
        ans+=1 #숫자가 1인 경우는 묶지 않으므로, 미리 계산한다.
    elif num>1:
        pos.append(num)
#목적에 맞게 정렬
neg.sort()
pos.sort(reverse=True)

#작은 수부터 차례대로 묶는다
for i in range(0,len(neg),2):
    if i+1<len(neg):
        ans+=neg[i]*neg[i+1]
    else:
        ans+=neg[i]

#큰 수부터 차례대로 묶는다
for i in range(0,len(pos),2):
    if i+1<len(pos):
        ans+=pos[i]*pos[i+1]
    else:
        ans+=pos[i]

print(ans)