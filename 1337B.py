import math
t = int(input())
for i in range(t):
    x,n,m = map(int,input().split())
    for j in range(n):
        x = math.floor(x/2)+10
    for k in range(m):
        x-=10
    if x<=0:
        print('YES')
    else:
        print('NO')