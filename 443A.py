sa = str(input())

lssa = []
for i in range(len(sa)):
    if i%3==1:
        lssa.append(sa[i])
ssa = set(lssa)
if len(lssa)>1:
    print(len(ssa))
else:
    print(0)