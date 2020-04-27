A = str(input())
B = str(input())
C = str(input())
D = str(input())
E = str(input())
a = A.find('1')
b = B.find('1')
c = C.find('1')
d = D.find('1')
e = E.find('1')
f = 0
if a>-1:
    print(2+(abs((a//2)-2)))
elif b>-1:
    print(1+(abs((b//2)-2)))
elif c>-1:
    print(0+(abs((c//2)-2)))
elif d>-1:
    print(1+(abs((d//2)-2)))
elif e>-1:
    print(2+(abs((e//2)-2)))