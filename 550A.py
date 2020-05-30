s = str(input())
ab = 0
ba = 0
ab+=s.find('AB')
s1 = s.replace('AB','')
ba+=s1.find('BA')
if ab>-1 and ba>-1:
    print('YES')
else:
    print('NO')