# n = int(input())
# mem = {}

# for i in range(1, n+1):
#     data = input()
#     mem[i] = data

# mem_sorted = dict(sorted(mem.items(), key=lambda x: (x[1][0:3], x[0])))

# for i in mem_sorted.values():
#     print(i)

n = int(input())
member_lst = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member_lst.append((age, name))

member_lst.sort(key = lambda x : x[0])	## (age, name)에서 age만 비교

for i in member_lst:
    print(i[0], i[1])
