import sys
from collections import Counter

N = int(sys.stdin.readline())
num_list = []

for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

avg = sum(num_list) / N

if f"{avg:.0f}" == "-0":
    print(0)
else:
    print(f"{avg:.0f}")


print(num_list[(N-1)//2]) #중앙값

num_count = Counter(num_list).most_common(2)
if N == 1:
    print(num_list[0])
elif num_count[0][1] == num_count[1][1]:
    print(num_count[1][0])
else:
    print(num_count[0][0])

print(max(num_list) - min(num_list))