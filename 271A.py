year = int(input())

while len(str(year+1)) != len(set(str(year+1))):
    year+=1
    continue
else:
    print(year+1)