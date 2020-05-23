n = int(input())
dima = 0
for i in range(n):
    a,b = map(int,input().split())
    if a==b:
        dima+=1
if dima==n:
    print('Poor Alex')
else:
    print('Happy Alex')