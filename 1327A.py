t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    if (n-k)%2==0:
        print('YES')
    else:
        print('NO')