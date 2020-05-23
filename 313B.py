s = str(input())
ls = list(s)
n = int(input())

for i in range(n):
    res = 0
    l,m = map(int,input().split())
    for i in range(l,m):
        if ls[i]==ls[i-1]:
            res+=1
        else:
            res+=0
    print(res)