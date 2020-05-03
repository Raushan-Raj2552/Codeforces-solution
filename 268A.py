n = int(input())
lshu = []
lsgu = []
for i in range(n):
    hu,gu = map(int,input().split())
    lshu.append(hu)
    lsgu.append(gu)
match = 0
for j in lshu:
    if j in lsgu:
        match+=lsgu.count(j)
print(match)