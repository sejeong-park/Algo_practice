#숫자 카드 게임
N,M=map(int,input().split())

result=0
# 한줄 씩 입력받아 확인
for i in range(N):
    data=list(map(int,input().split()))
    #현재 줄에서 가장 작은 값 찾기
    min_value=min(data)
    #가장 작은 수 들 중에서 가장 큰 수 찾기
    result=max(result,min_value)

print(result)