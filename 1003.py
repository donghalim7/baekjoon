import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    zero = [1, 0]
    one = [0, 1]


    if n <= 1:
        print(zero[n], one[n])
    else:
        for i in range(2, n+1):
            zero.append(zero[i-2] + zero[i-1])
            one.append(one[i-2] + one[i-1])

        print(zero[n], one[n])