t = int(input())
for i in range(t):
    a,b,c,n = map(int,input().split())
    if (a+b+c+n)%3==0:
        print('YES')
    else:
        print('NO')