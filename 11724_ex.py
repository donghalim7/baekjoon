import sys
sys.setrecursionlimit(10000)

def dfs(x):
    visited[x] = True
    for i in connection[x]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
connection = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)