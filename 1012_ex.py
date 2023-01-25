#DFS
import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정

T = int(sys.stdin.readline()) # 테스트 케이스 받는 부분

dx = [-1, 1, 0, 0] # 상하좌우 이동하여 계산하기 위한 list
dy = [0, 0, -1, 1]

def dfs(x, y):
  if x <= -1 or x >= N or y<= -1 or y>= M:
    return False

  if graph[x][y] == 1:
    graph[x][y] = 0

    for i in range(4):
      dfs(x + dx[i], y+dy[i])

    return True
  return False

answer = []
for _ in range(T):
  M, N, K = list(map(int, sys.stdin.readline().split()))  

  graph = [[0]*M for _ in range(N)]

  for _ in range(K):
    x, y = map(int, input().split())
    graph[y][x] = 1

  cnt = 0
  for i in range(N):
    for j in range(M):
      if dfs(i, j):
        cnt +=1

  print(cnt)

#BFS
# import sys
# from collections import deque
# def bfs(y,x): # 영역 확인
#     q = deque()
#     q.append((y,x))
#     while q:
#         now = q.popleft()
#         for l in range(4): # 사방면 확인
#             hh = now[0] + dh[l]
#             ww = now[1] + dw[l]
#             if 0 <= ww < w and 0 <= hh < h and graph[hh][ww] == 1:
#                 graph[hh][ww] = 0
#                 q.append((hh,ww))

# if __name__ == "__main__":
#     dw = [0,1,0,-1] # 북, 동, 남, 서
#     dh = [-1,0,1,0]
#     read = sys.stdin.readline
#     T = int(read())
#     for _ in range(T):
#         w, h, k = map(int,read().split())
#         graph = [[0]*w for _ in range(h)]
#         result = 0
#         for _ in range(k): # 배추 위치 입력
#             x,y = map(int,read().split())
#             graph[y][x] = 1
#         for i in range(h):
#             for j in range(w):
#                 if graph[i][j] == 1:
#                     graph[i][j] = 0
#                     bfs(i,j)
#                     result += 1 # 영역 수
#         print(result)