import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

coin = []
cnt = 0

for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

coin = coin[::-1]

for i in coin:
    if i > k:
        continue
    else:
        cnt += k // i
        k = k - (k // i) * i

        if k == 0:
            break

print(cnt)