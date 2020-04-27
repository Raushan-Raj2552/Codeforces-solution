a,b = map(int,input().split())
c = input().split()
d = 0
for i in c:
    if int(i)>b:
        d+=1
print(d)