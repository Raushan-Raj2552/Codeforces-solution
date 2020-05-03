a = int(input())
b = input().split()

resp = 0
for i in range(len(b)):
    if int(b[int(i)])>0:
        resp+=1
    else:
        resp+=0

if resp!=0:
    print('HARD')
else:
    print('EASY')