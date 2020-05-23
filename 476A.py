n,m = map(int,input().split())
ans = []
for i in range((n+1)//2,n+1):
    if i%m==0:
        ans.append(i)
if len(ans)>0:
    print(ans[0])
else:
    print(-1)