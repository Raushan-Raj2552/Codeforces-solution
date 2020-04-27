a = int(input())
for i in range(a):
    b,c,d,e = map(int,input().split())
    f = (c-b)/(d+e)
    if f%1==0:
        print(int(f))
    else:
        print('-1')