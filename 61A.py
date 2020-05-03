a = str(input())
b = str(input())
c = ''
for i in range(len(a)):
    c+= str(int(a[i]) ^ int(b[i])) #xor
print(c)