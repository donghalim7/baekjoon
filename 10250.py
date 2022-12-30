case = int(input())

for i in range(case):
    h, w, n = map(int, input().split())
    room_list = []
    for j in range(1, w+1):
        for k in range(1, h+1):
            room_list.append(k * 100 + j)

    print(room_list[n-1])