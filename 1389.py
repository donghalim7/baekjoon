import sys

input = sys.stdin.readline


n, m = map(int, input().split())

friend_list = [[] for _ in range(n+1)]

for _ in range(n):
    a, b = map(int, input().split())
    friend_list[a].append(b)
    friend_list[b].append(a)

res = [0] * (n+1) # 케빈 베이컨의 수 넣을 리스트

for i in range(n): # 1~n까지 돌림. 예를 들어 1 기점의 2를 찾고싶으면 인덱스 2에 1이 있는지 확인, 없으면 타고 타고 가는 방식
    
    sum = 0
    for j in range(n):


print(friend_list)