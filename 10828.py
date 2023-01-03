import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
dq = deque()

for i in range(N):
    cmd = list(sys.stdin.readline().rstrip().split())
    if cmd[0] == "push":
        dq.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif cmd[0] == "size":
        print(len(dq))
    elif cmd[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == "top":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])