import sys

n, k = map(int, sys.stdin.readline().split())

queue = [i for i in range(1, n + 1)]
li = []
index = 0 # 제거할 인덱스

while queue:
    # 제거할 인덱스를 더해서 제거할 인덱스 위치를 바꾼다.
    index += k - 1

    # 인덱스의 크기가 남은 큐에 길이보다 크다면
    if index >= len(queue):
        # 인덱스의 크기를 나눠 나머지로 바꾼다.
        # 한바퀴 돌았기 때문
        index %= len(queue)

    # 큐에서 해당 인덱스를 제거하고 제거한 요소를 리스트에 추가한다.
    li.append(str(queue.pop(index)))

print("<", end="")
print(", ".join(li), end="")
print(">")