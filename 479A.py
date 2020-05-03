a = int(input())
b = int(input())
c = int(input())

valu = []
valu.append(a*b*c)
valu.append(a+b+c)
valu.append(a*b+a*c)
valu.append(a*b+b*c)
valu.append(a*c+b*c)

print(max(valu))
