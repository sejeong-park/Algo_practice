#방 배정
#N은 수학여행에 참가하는 인원 수
#K는 한 방에 배정할 수 있는 최대 인원 수
#성별 S-> 성별 여자일 경우 0, 남자일 경우 Y, 학년 Y
import math
N,K=map(int, input().split())
student=[[0 for _ in range(7)] for _ in range(2)]

for _ in range(N):
    S,Y=map(int,input().split())
    student[S][Y]+=1
room=0
for gender in student:
    for classes in gender:
        div,mod=divmod(classes,K)
        #두 숫자를 묶어서 첫번째 인자를 두번째 인자로 나눈 몫과 나머지를 tuple
        if mod>0:
            div+=1
        room+=div

print(room)

#N,M=map(int, input().split())
#student=[[0]*7 for _ in range(3)] #성별/ 학년 별

#or _ in range(N):
 #   S,Y=map(int, input().split())
 #   student[S][Y]+=1

#room=0
#for i in student:
 #   for j in i:
  #      room+=math.ceil(j.k)

#print(room)