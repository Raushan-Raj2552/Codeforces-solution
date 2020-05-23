a = int(input())

pos = str(input())
lspos = list(pos)
pwd = str(input())
lspwd = list(pwd)

res = 0
for i in range(a):
    e = abs(int(lspos[i])-int(lspwd[i]))
    if e<=5:
        res+=e
    else:
        res+=(10-e)
print(res)