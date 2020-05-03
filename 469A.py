n = int(input())
p = input().split()
q = input().split()
lsp = list(p)
lsp.remove(lsp[0])
lsq = list(q)
lsq.remove(lsq[0])
lspq = lsp+lsq
lspq.sort()
if int(lspq[-1])>=n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")