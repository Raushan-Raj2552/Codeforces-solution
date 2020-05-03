alpha = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
a = str(input())
b = a.lower()
ls = []

for i in alpha:
    if i in b:
        ls.append(1)
    else:
        ls.append(0)

if sum(ls)!=26:
    print('NO')
else:
    print('YES')