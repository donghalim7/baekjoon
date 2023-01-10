import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

login = dict()

for _ in range(n):
    i, p = sys.stdin.readline().rstrip().split()
    login[i] = p

for _ in range(m):
    id = sys.stdin.readline().rstrip()
    print(login[id])