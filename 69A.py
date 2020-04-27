a = int(input())
B = 0
C = 0
D = 0
for i in range(a):
    b,c,d = map(int,input().split())
    B+=b
    C+=c
    D+=d
if B==0 and C==0 and D==0:
    print('YES')
else:
    print('NO')