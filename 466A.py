n,m,a,b = map(int,input().split())
if b/m<a:
    print(((n//m)*b)+((n%m)*a))
else:
    print(n*a)