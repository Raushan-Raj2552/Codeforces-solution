import math as m
a,b,n = map(int,input().split())
simon = 0
antisimon = 0
while n>0:
    n-=(m.gcd(a,n))
    if n==0:
        print(0)
    n-=(m.gcd(b,n))
    if n==0:
        print(1)
