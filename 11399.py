import sys
from itertools import *

n = int(sys.stdin.readline().rstrip())

time = list(map(int, sys.stdin.readline().rstrip().split()))
time_list = list(permutations(time, n))


total_time_set = set()

for k in time_list:
    total_time = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            total_time += k[j-1]
    total_time_set.add(total_time)


print(min(total_time_set))