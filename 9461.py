t = int(input())

for _ in range(t):
    p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    n = int(input())

    if n <= 10:
        print(p[n-1])
    else:
        for i in range(n-10):
            p.append(p[i+5] + p[i+9])
        print(p[-1])