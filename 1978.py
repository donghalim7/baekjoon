n = int(input())
numlist = list(map(int, input().split()))
cnt = 0 # 소수의 개수

for i in numlist:
    numcnt = 0

    if i == 1:
        continue
    else:
        for j in range(1, i+1):
            if i % j == 0:
                numcnt += 1

        if numcnt == 2:
            cnt += 1

print(cnt)