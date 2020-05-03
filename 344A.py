n = int(input())

joint = 0

magnet = []
for i in range(n):
    pole = int(input())
    magnet.append(pole)

for i in range(1,n):
    if int(magnet[i-1])+int(magnet[i])==11:
        joint+=1
print(joint+1)