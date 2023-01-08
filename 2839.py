import sys

N = int(sys.stdin.readline())

combi_list = []

for i in range(N//3 + 1):
    k = (N - 3*i) // 5
    
    if 3*i + 5*k == N:
        combi_list.append(i+k)

if len(combi_list) == 0:
    print(-1)
else:
    print(min(combi_list))