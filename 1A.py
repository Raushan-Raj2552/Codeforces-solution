import math as ma
n,m,a = map(int,input().split())
number = ma.ceil(n/a)+ma.ceil(m/a)
print(number)