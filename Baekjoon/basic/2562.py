#최댓값
#최댓값이 몇 번째 수인지

num=[]
for i in range(9):
    num.append(int(input()))

print(max(num))
print(num.index(max(num))+1)