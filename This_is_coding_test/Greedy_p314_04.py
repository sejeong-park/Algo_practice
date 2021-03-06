#만들 수 없는 금액
#잘 모르겠음

N=input()
coin=list(map(int,input().split()))
coin.sort()

target=1 #만들 수 없는 금액

for x in coin:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target<x:
        break
    target+=x
#만들 수 없는 금액 출력
print(target)


