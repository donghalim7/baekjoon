import sys
import heapq

n = int(sys.stdin.readline().rstrip())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())

    if x != 0:
        heapq.heappush(heap, (-1) * x)
    else:
        try:
            print(-heapq.heappop(heap))
        except:
            print(0)