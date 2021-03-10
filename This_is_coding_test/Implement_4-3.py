#왕실의 나이트

# 1) 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2) 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

#행의 위치 1~8
#열의 위치 a~h

input_data=input()
row=int(input_data[1]) #행 => 숫자
column=int(ord(input_data[0])) #열 (알파벳-> 숫자)
#ord() : ord함수: 특정 문자를 아스키 코드로 변환해주는 함수

#나이트가 이동할 수 있는 8가지 방향 정의
steps=[(-2,-1),(-1,-2),(1,-2),(2,1),(1,2),(-1,2),(-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result=0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row=row+step[0]
    next_column=column+step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row>=1 and next_row<=8 and next_column >=1 and next_column<=8:
        result+=1

print(result)