a = int(input())
b = 0
c = []
for i in range(a):
    d,e = map(int,input().split())
    b+=(e-d)
    c.append(b)
print(max(c))