a = int(input())
b = []
for i in range(a):
    c,d = map(int,input().split())
    if d-c>=2:
        b.append(i)
print(len(b))