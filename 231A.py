a = int(input())
b = 0
for i in range(a):
    c,d,e = map(int,input().split())
    if c+d+e>=2:
        b+=1
print(b)