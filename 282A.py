a = int(input())
b = 0
c = 0
for i in range(a):
    e = str(input())
    b+=(e.count('+')/2)
    c+=(e.count('-')/2)
print(int(b-c))