n,k = map(int,input().split())
ls = []
for i in range(1,n+1):
    if i%2==1:
        ls.append(i)
for j in range(1,n+1):
    if j%2==0:
        ls.append(j)
print(ls[k-1])