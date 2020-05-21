n,k = map(int,input().split())
time = (240-k)//5
ls = []
for i in range(n):
    if i*(i+1)/2<=time:
        ls.append(i)
print(len(ls))