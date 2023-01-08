import sys

N = int(sys.stdin.readline())

dot = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dot.append((x, y))

sorted_dot = sorted(dot, key = lambda x: (x[1], x[0]))

for a, b in sorted_dot:
    print(a, b)