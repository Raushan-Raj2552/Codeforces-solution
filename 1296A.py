t = int(input())
for i in range(t):
    n = int(input())
    a = map(int,input().split())
    sa = sum(a)
    if sa%2==1:
        print('YES')
    else:
        print('NO')