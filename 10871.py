n, x = map(int, input().split())
numlist = list(map(int, input().split()))

for i in numlist:
    if i < x:
        print(i, end=" ")