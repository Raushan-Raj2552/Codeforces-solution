n = int(input())
point = map(int,input().split())
lspt = list(point)
amaze = 0
for i in range(len(lspt)-1):
    if lspt[i+1]-lspt[i]>=0:
        amaze+=1
print(amaze)