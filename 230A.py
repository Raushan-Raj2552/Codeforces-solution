s,n = map(int,input().split())
ls = []
for i in range(n):
    s1 = s
    x,y = map(int,input().split())
    if x<=s1:
        s1-=(x-y)
        if s1>0:
            ls.append(s1)
        else:
            ls.append(0)
    else:
        ls.append(0)
ls.remove(ls[-1])
zero = ls.count(0)
if zero>0 or len(ls)==0:
    print('NO')
else:
    print('YES')