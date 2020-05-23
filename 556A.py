n = int(input())
s = str(input())
if len(s)==n:
    lss = list(s)
    one = lss.count('1')
    zero = lss.count('0')
    print(abs(one-zero))