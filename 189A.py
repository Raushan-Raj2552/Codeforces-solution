n,a,b,c = map(int,input().split())
if a+b+c == n:
    print(3)
elif a+b==n or b+c==n or a+c==n:
    print(2)
elif a==n or b==n or c==n:
    print(1)