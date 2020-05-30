t = int(input())
for i in range(t):
    n = int(input())
    a = map(int,input().split())
    lsa = list(a)
    ssa = set(lsa)
    print(len(ssa))