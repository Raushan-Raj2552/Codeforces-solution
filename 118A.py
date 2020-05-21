a = str(input())
a1 = a.lower()
a2 = a1.replace('a','')
a3 = a2.replace('e','')
a4 = a3.replace('i','')
a5 = a4.replace('o','')
a6 = a5.replace('u','')
a7 = a6.replace('y','')

lsa6 = list(a6)

strout = '.'
for i in lsa6:
    strout+=i+'.'
print(strout[:-1])