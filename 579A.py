import math as m
x = int(input())
n = m.log2(x)
n1 = m.floor(n)
print(x+1-(2**n1))