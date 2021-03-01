#주사위 세개

n,m,k=list(map(int,input().split()))

if n==m==k:
    print(10000+n*1000)
elif n==m:
    print(1000+n*100)
elif n==k:
    print(1000+n*100)
elif m==k:
    print(1000+m*100)
else:
    print(max(n,m,k)*100)