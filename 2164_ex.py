# import sys

# N = int(sys.stdin.readline())

# card = [i for i in range (1, N+1)]

# while len(card) > 1:
#     del card[0] #앞의 것 삭제

#     if len(card) == 1:
#         break

#     card.append(card[0]) #앞의 것을 뒤로 옮기는 과정
#     del card[0]

# print(card[0])

# 시간 초과

from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) >1):
    deque.popleft()
    deque.rotate(-1)
    
print(deque[0])

# import sys

# N = int(sys.stdin.readline())

# arr = [i+1 for i in range(N)]

# while len(arr) > 1:
#     if len(arr) % 2:
#         t = [arr[-1]]
#         t.extend(arr[1::2])
#         arr = t
#     else:
#         arr = arr[1::2]
        

# print(arr[0])

# deque를 사용하지 않은 방법