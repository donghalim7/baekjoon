n, m = map(int, input().split())
k = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = k[i] + k[j] + k[k]
            if sum > m:
                continue
            else:
                result = max(result, sum)

print(result)