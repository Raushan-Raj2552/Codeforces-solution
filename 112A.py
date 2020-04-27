a = 'abcdefghijklmnopqrstuvwxyz'
B = str(input())
C = str(input())
b = B.lower()
c = C.lower()
d = 0
e = 0
for i in b:
    d+=(a.find(i))
for j in c:
    e+=(a.find(j))
if d>e:
    print('1')
elif d==e:
    print('0')
elif d<e:
    print('-1')