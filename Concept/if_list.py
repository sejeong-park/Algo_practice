a=[1,2,3,4,5,5,5]
remove_set={3,5}

result=[]
for i in a:#i가 a의 반복문일 때
    if i not in remove_set:#remove_set에 없는 i는
        result.append(i)#result에 저장
print(result)

#같은 코드
a=[1,2,3,4,5,5,5]
remove_set={3,5}

result=[i for i in a if i not in remove_set]
print(result)