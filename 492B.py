n,l = map(int,input().split())
ai = map(int,input().split())
pos = list(ai)
pos.sort()
dist = []
for i in range(1,len(pos)):
    dist.append(int(pos[i])-int(pos[i-1]))
dist.sort()
if dist[-1]>(pos[0]*2):
    print("%0.10f"%(dist[-1]/2))
else:
    print("%0.10f"%(pos[0]))