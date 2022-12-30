# n = int(input())
# numlist = []

# for i in range(n):
#     num = int(input())
#     numlist.append(num)

# numlist.sort()

# for i in numlist:
#     print(i)

#for문 속에서 append를 사용하면 메모리 재할당이 이루어져 메모리를 효율적으로 사용하지 못함

import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)