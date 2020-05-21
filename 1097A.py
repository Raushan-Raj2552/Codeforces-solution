table = str(input())
hand = input().split()
move = 0
for i in hand:
    if i[0]==table[0] or i[1]==table[1]:
        move+=1
    else:
        move+=0
if move>0:
    print('YES')
else:
    print('NO')