t = int(input())

for i in range(t):
    amount = 0
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    amount+=(abs(y-x)*a)
    amount+=(min(x,y)*b)
    print(amount)