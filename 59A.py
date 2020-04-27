upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnpoqrstuvwxyz'
a = str(input())
b = 0
c = 0
aup = a.upper()
alo = a.lower()
for i in  upper:
    b += a.count(i)
for j in lower:
    c += a.count(j)
if b>c:
    print(aup)
else:
    print(alo)