import sys

N = int(sys.stdin.readline())

body = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    body.append((x,y))


for i in body:
    rank = 1
    
    for j in body:
        