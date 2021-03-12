#문자열 재정렬

S=input()
alpha=[]
sum=0
#문자를 하나씩 확인
for i in S:
    #알파벳인 경우 alpha 리스트에 삽입
    if i.isalpha():
        alpha.append(i)
    # 숫자는 따로 더하기
    else:
        sum+=int(i)

#알파벳을 오름차순으로 정렬
alpha.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if sum!=0:
    alpha.append(str(sum))

#최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(alpha))

