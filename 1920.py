import sys

n = int(sys.stdin.readline())
n_num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_num = list(map(int, sys.stdin.readline().split()))

for i in m_num:
    if i in n_num:
        print(1)
    else:
        print(0)

#시간초과