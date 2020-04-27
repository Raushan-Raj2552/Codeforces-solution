a = int(input())
if a%4==0:
    print('YES')
elif a%7==0:
    print('YES')
else:
    result = []
    ls = []
    for i in range(2,a+1):
        if a%i==0:
            ls.append(i)
    for j in range(len(ls)):
        c=str(ls[j])
        x = c.count('4')
        y = c.count('7')
        if x>0 and y>0:
            result.append('TRUE')
        else:
            result.append('FALSE')

    B = result.count('TRUE')
    if B==0:
        print('NO')
    else:
        print('YES')