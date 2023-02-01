from collections import deque
n,k=map(int,input().split())
dq=deque()
time=[0]*100001
def bfs():
    dq.append(n)
    while dq:
        now=dq.popleft()
        if now==k:
            print(time[now])
            return
        for next in (now-1,now+1,now*2):
            if 0<=next<100001 and time[next]==0:
                time[next]=time[now]+1
                dq.append(next)
bfs()