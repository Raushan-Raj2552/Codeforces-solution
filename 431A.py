a1,a2,a3,a4 = map(int,input().split())

s = str(input())
ls = list(s)

one = 0
two = 0
three = 0
four = 0

for i in ls:
    if i=='1':
        one+=1
    elif i=='2':
        two+=1
    elif i=='3':
        three+=1
    elif i=='4':
        four+=1

print(one*a1+two*a2+three*a3+four*a4)