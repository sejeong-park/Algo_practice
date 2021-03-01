#숫자

a,b=map(int,input().split())
if a!=b:
    if a>b:
        a,b=b,a
    print(b-a-1)
    print(*range(a+1,b))
else:
    print(0)

#*range(a,b) a~b까지 숫자를 쭉 보여짐