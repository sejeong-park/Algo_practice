#시각

#00시 00분 00초부터 N시 59분59초까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수

N=int(input())

count=0

for i in range(N+1):#시
    for j in range(60):#분
        for k in range(60): #초
            #매 시각 안에  3이 포함되어 있다면 카운트 증가
             if '3' in str(i)+str(j)+str(k):
                 count+=1

print(count)