t = int(input())
for i in range(t):
    n = int(input())
    a = len(str(n))
    
    ls1 = []
    for i in range(1,a+1):
        ls1.append(n%(10**i))
    
    ls2 = []
    for j in range(1,len(ls1)):
        ls2.append(ls1[j]-ls1[j-1])
    
    ls2.append(ls1[0])
    
    ls3 = []
    for k in ls2:
        if k!=0:
            ls3.append(k)
    print(len(ls3))
    print(*ls3)# for prinnting all elements of a list in single line.