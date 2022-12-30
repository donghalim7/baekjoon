n = int(input())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[0], x[1]))

for i in data:
    # print(str(i)[1:-1])
    print(" ".join(str(j) for j in i))