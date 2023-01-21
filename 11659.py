import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numlist = list(map(int, sys.stdin.readline().rstrip().split()))
sumlist = [0]


s = 0
for i in numlist:
    s += i
    sumlist.append(s)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    
    print(sumlist[j] - sumlist[i-1])