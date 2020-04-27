a,b = map(int,input().split())
c = 1
while True:
   if (a*(3**c))<=(b*(2**c)):
       c+=1
       continue
   else:
       print(c)
       break