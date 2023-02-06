numlist = input().split("-")

res = 0

for i in range(len(numlist)):
    inum = map(int, numlist[i].split("+"))
    if i == 0:
        res += sum(inum)
    else:
        res -= sum(inum)

print(res)