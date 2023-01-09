import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

tree.sort()

start, end = 1, max(tree)

while start <= end:
    mid = (start+end)//2
    wood = 0

    for i in tree:
        if i > mid:
            wood += i - mid
        
    if wood >= M:
        start = mid + 1
    else:
        end = mid - 1


print(end)