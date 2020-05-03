n,m = map(int,input().split())
ai = input().split()
lsai = list(ai)
dist = (int(lsai[0])-1)

for i in range(len(lsai)-1):
    if int(lsai[i+1])>=int(lsai[i]):
        dist+=(int(lsai[i+1])-int(lsai[i]))
    elif int(lsai[i+1])<int(lsai[i]):
        dist+=(n+int(lsai[i+1])-int(lsai[i]))

print(dist)