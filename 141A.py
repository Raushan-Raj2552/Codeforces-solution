a = str(input())
b = str(input())
c = str(input())
lsab = list(a)+list(b)
lsab.sort()
lsc = list(c)
lsc.sort()
if lsab == lsc:
    print('YES')
else:
    print('NO')