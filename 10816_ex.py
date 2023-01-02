# import sys

# N = int(sys.stdin.readline())
# N_num = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# M_num = list(map(int, sys.stdin.readline().split()))

# for i in M_num:
#     count = N_num.count(i)
#     print(count, end=" ")

from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

hash = {}

for i in card:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in test:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')