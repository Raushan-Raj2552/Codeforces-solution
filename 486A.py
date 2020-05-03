n = int(input())
ls = []
ls1 = []
for i in range(1,n+1):
    if i%2==1:
        ls.append(i)
for j in range(1,n+1):
    if j%2==0:
        ls1.append(j)
print(sum(ls1)-sum(ls))