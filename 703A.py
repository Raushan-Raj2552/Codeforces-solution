n = int(input())
m = 0
c = 0
for i in range(n):
    mi,ci = map(int,input().split())
    m+=mi
    c+=ci
if m>c:
    print('Mishka')
elif c>m:
    print('Chris')
else:
    print('Friendship is magic!^^')