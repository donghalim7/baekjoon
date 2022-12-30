#1+6+12+18+24

n = int(input())


sum = 1
init = 0
count = 1
while sum < n:
    init = 6 * count
    sum += init
    count += 1


print(count)