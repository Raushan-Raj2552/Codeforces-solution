a = int(input())
b = input().split()

lsb1 = list(b)

lsb = list(b)
lsb.sort()

min = lsb1[::-1].index(lsb[0])
max = lsb1.index(lsb[-1])

if min+max<len(lsb):
    print(min+max)
else:
    print(min+max-1)