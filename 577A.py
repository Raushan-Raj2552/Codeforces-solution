n,x = map(int,input().split())

ls = []
for i in range(1,n+1):
    for j in range(1,n+1):
        ls.append(i*j)

print(ls.count(x))