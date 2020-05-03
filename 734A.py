game = int(input())
result = str(input())

a=result.count('A')
d=result.count('D')

if a>d:
    print('Anton')
elif d>a:
    print('Danik')
else:
    print('Friendship')

