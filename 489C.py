m,s = map(int,input().split())
ls1 = []
for i in range(10**(m-1),int('9'*m)):
    j = str(i)
    ls1.append(j)

ls2 = []   
for j in ls1:
    sum = 0
    for k in range(len(j)):
        sum+=int(j[k])
        if sum ==s:
            ls2.append(j)
if len(ls2)>=2:
    print(ls2[0],ls2[-1])
else:
    print(-1,-1)