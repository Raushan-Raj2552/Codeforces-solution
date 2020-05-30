k = int(input())
a = map(int,input().split())
lsa = list(a)
ans = 0
while True:
    if k>0:
        k-=max(lsa)
        lsa.remove(max(lsa))
        ans+=1
    else:
        break
print(ans)