n,h = map(int,input().split())
heit = input().split()

ans = 0

for i in range(len(heit)):
    if int(heit[int(i)])>h:
        ans+=2
    else:
        ans+=1
print(ans)