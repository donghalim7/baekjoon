import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())

tomatolist = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

res = 0

for i in range(n):
    for j in range(m):
        if tomatolist[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and tomatolist[nx][ny] == 0:
                tomatolist[nx][ny] = tomatolist[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in tomatolist:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        
    res = max(res, max(i))

print(res - 1)