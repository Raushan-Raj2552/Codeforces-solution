a = int(input())
b = str(input())
c = 0
for i in range(1,len(b)):
    if b[i]==b[i-1]:
        c+=1
print(c)