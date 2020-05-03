n = int(input())
bill = 0

bill+=(n//100)
n1 = n%100
bill+=(n1//50)
n2 = n1%50
bill+=n2//20
n3 = n2%20
bill+=n3//10
n4 = n3%10
bill+=n4//5
n5 = n4%5
bill+=n5
print(bill)