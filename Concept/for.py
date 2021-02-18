# for 변수 in 리스트: -> in 뒤에 오는 데이터 : 리스트, 튜플, 문자열 등
#   실행할 소스코드

result=0

#i는 1부터 9까지 모든 값을 순회
for i in range(1,10):
    result=result+i

print(result)

scores=[90,85,77,65,97]

for i in range(5):
    if scores[i]>=80:
        print(i+1,"번 학생은 합격입니다")

print("\n")
#반복문 안에서 continue를 만나면 프로그램의 흐름은 반복문의 처음으로 돌아간다.


score=[90,85,77,65,97]
cheating_list=[2,4]#2번학생과 4번학생이 컨닝함=> 점수가 높아도 합격 못해

for i in range(5):
    if i+1 in cheating_list:#만약 2번[1]은 리스트에 있는데 1값이 들어왔어, 그러면 반복문의 처음으로 돌아가기 때문에 2값(3번)의 포문으로 넘어가버림
        continue            #즉 생략
    if score[i]>=80:
        print(i+1,"번 학생은 합격입니다.")