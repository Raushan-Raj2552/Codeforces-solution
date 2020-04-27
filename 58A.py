a = str(input())
a1 = a[::-1]
h = a.find('h')
e = a.find('e')
l1 = a.find('l')
o = a.find('o')
l2 = 0
for i in range(l1+1,o):
    l2 +=1
if h<e<l1<o and l2>0:
    print('YES')
else:
    print('NO')