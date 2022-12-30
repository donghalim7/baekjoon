L = int(input())
arr = input()
hash = 0
count = 0

for i in arr:
    hash += (ord(i) - 96) * (31 ** count)
    count += 1

print(hash % 1234567891)