p = str(input())
h = p.find('H')
q = p.find('Q')
n9 = p.find('9')
plus = p.find('+')
if h+q+n9+plus>-4:
    print('YES')
else:
    print('NO')