t = int(input())
for i in range(t):
    n = int(input())
    a = map(int,input().split())
    lsa = list(a)
    ssa = set(lsa)
    if len(lsa)>len(ssa) and n>1:
        print(min(len(lsa)//2,len(ssa)))
    elif len(lsa)==len(ssa) and n>1:
        print(1)
    elif n==1:
        print(0)