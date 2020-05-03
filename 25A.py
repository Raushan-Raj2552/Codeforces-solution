a = int(input())
b = map(int,input().split())
lsb = list(b)

even = []
odd = []
for i in lsb:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
if len(even)==1:
    print(lsb.index(even[0])+1)
else:
    print(lsb.index(odd[0])+1)