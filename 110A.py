a = str(input())
b = a.count('0')
c = a.count('1')
d = a.count('2')
e = a.count('3')
f = a.count('4')
g = a.count('5')
h = a.count('6')
i = a.count('7')
j = a.count('8')
k = a.count('9')
A = f+i
B = b+c+d+e+g+h+j+k
if A>0 and B==0:
    print('YES')
else:
    print('NO')