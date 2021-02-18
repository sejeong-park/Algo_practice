#문제를 풀다보면 입력을 최대한 빠르게 받아야하는 경우
#흔히 정렬, 이진 탐색, 최단 경로 문제
#입력의 개수가 많은 경우는 단순히 input()함수를 그대로 사용하지 않음

#input()함수는 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있다!!!!

#파이싼의 sys 라이브러리에 정의되어 있는 sys.stdin.readline()함수 이용!!!
#sys 라이브러리는 다음과 같은 방식으로 사용하며 input()함수와 같이 한 줄씩 입력 받기 위해 사용됨

#import sys
#sys.stdin.readline().rstrip()

#sys 라이브러리를 사용할 때 한 줄 입력을 받고나서 rstrip() 함수를 꼭 호출해야한다.
# 왜? -> readline()로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 공백 문자를 제거하려면 rstrip()함수를 사용해야함-> 그 C언어에서 커서처럼
#외우기!!!!

import sys
data=sys.stdin.readline().rstrip()
print(data)