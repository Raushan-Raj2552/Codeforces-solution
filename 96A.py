a = str(input())
b = a.find('0000000')
c = a.find('1111111')
if b>-1 or c>-1:
    print('YES')
else:
    print('NO')