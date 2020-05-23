n = int(input())

lsprice = []
price = input().split()
for i in price:
    lsprice.append(int(i))

days = int(input())
for i in range(days):
    spent = int(input())
    out = 0
    for j in range(len(lsprice)):
        if lsprice[j]<=int(spent):
            out+=1
    print(out)