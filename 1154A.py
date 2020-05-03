lsx = []
x1,x2,x3,x4 = map(int,input().split())
lsx.append(x1)
lsx.append(x2)
lsx.append(x3)
lsx.append(x4)
lsx.sort()
print(lsx[3]-lsx[2],lsx[3]-lsx[1],lsx[3]-lsx[0])