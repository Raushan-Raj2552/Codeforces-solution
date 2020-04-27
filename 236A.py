a = str(input())
b = ''
for i in a:
    if i not in b:
        b+=i
c = len(b)
if c%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')