a = int(input())
b = input().split()
lsb = list(b)
lsb.sort()
result = ''
for i in range(len(lsb)):
    result+=str(lsb[i])+' '
print(result[:-1])