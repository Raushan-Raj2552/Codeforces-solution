n = int(input())
a = 5**n
a1 = '00'+str(a) # 00 for the value of a=0 and a=1
print(a1[-2]+a1[-1])