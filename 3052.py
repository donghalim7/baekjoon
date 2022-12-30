numlist = [int(input()) for _ in range(10)]
remlist = []
for i in numlist:
    remlist.append(i % 42)

print(len(set(remlist)))