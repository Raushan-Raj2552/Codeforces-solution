m,n = map(int,input().split())
toys = input().split()

ls = []
for i in range(len(toys)):
    ls.append(int(toys[int(i)]))
ls.sort()
result = []
for j in range(0,len(ls)-m):
    result.append(ls[j+m-1]-ls[j])

print(min(result))