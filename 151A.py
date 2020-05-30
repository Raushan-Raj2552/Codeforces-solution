n,k,l,c,d,p,nl,np = map(int,input().split())

drink = (k*l)//nl
limes = c*d
salt = p//np

toast = min(drink,limes,salt)
print(toast//n)#Each friend will prepare equal number of toast