import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

hear = set()
see = set()

for _ in range(n):
    hear.add(sys.stdin.readline().rstrip())

for _ in range(m):
    see.add(sys.stdin.readline().rstrip())
    
hear_see = list(hear.intersection(see)) #list(hear&see)
hear_see.sort()

print(len(hear_see))
for i in hear_see:
    print(i)