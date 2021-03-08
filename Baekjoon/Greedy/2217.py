#로프
#N개의 로프

N=int(input())
rope=[]

for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True) #내림차순

value=[]
for num in range(N):
    value.append(rope[num]*(num+1))
print(max(value))