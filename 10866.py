import sys
from collections import deque

dq = deque()

N = int(input())

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_front":
        dq.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        dq.appendleft(int(cmd[1]))
    elif cmd[0] == "pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif cmd[0] == "pop_back":
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
    elif cmd[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])

    elif cmd[0] == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
       