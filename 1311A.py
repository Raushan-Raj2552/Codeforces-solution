t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    c = b-a
    if (c>0 and c%2==1) or (c<0 and c%2==0):
        print(1)
    elif (c<0 and c%2==1) or (c>0 and c%2==0):
        print(2)
    elif c==0:
        print(0)