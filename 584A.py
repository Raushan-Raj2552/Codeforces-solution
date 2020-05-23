import random as r
n,t = map(int,input().split())
lsno = []
for i in range(10**(n-1),int('9'*n)):
    if i%t==0:
        lsno.append(i)
out = r.choices(lsno)
print(*(out))