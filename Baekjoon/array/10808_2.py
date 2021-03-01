#문자열 처리 연습
ip=input()
alp="abcdefghijklmnopqrstuvwxyz"
result={}
for a in alp:
    result[a]=ip.count(a)

string=""
for v in result.values():
    string += str(v)+" "
print(string.rstrip())