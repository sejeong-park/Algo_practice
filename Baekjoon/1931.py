n=int(input())

#끝나는 시간이 가장 빠른 순으로 정렬
#시작하는 시간의 오름차순

input_arr=[] #input array

for i in range(n):
    A,B=map(int,input().split())
    input_arr.append([A,B])

input_arr.sort(key=lambda x:(x[1],x[0]))

def solution(input_arr):
    answer=0
    endTime=0
    for i in range(len(input_arr)):
        if endTime<=input_arr[i][0]:
            endTime=input_arr[i][1]
            answer+=1
    return answer

print(solution(input_arr))
