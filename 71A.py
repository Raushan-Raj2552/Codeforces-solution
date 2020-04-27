a = int(input())
for i in range(a):
    b = input()
    if len(b)<=4:
        print(b)
    else:
        print(b[0]+str(len(b)-2)+b[-1])