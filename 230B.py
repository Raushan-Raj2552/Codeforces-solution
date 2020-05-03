n = int(input())
x = map(int,input().split())
lsx = list(x)
for i in lsx:
    div = 0
    for j in range(1,i+1):
        if i%j==0:
            div+=1
    if div==3:
        print('YES')
    else:
        print('NO')