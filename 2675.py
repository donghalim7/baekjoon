case = int(input())

for i in range(case):
    R, S = input().split()
    for i in list(S):
        print(int(R) * i, end = "")

    print()