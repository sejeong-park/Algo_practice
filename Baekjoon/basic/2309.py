#일곱난쟁이
import sys

TAERGET_NUM=100

#전체합구하기
sum=0
data=[]
for _ in range(9):
    temp=int(sys.stdlin.readline())
    data.append(temp)
    sum+=temp

#오름차순정렬
data=sorted(data)

#2개를 빼서 비교
for i in range(9):
    for j in range(9):
        temp=data[i]+data[j]
        if sum-temp==TARGET_NUM:
            data.remove(i)
            data.remove
            for k in range(9):
                if k!=i and k!=j:
                    print(data[k])
            sys.exit()