n = int(input())
numlist = []

for i in range(n):
    num = int(input())
    numlist.append(num)

numlist.sort()

for i in numlist:
    print(i)