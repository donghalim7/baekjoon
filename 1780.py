import sys

input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
neg_cnt = 0
zero_cnt = 0
pos_cnt = 0

def sol(x, y, n):
    global neg_cnt, zero_cnt, pos_cnt
    col = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if col != paper[i][j]:
                sol(x, y, n//3)
                sol(x, y+n//3, n//3)
                sol(x, y+(n//3)*2, n//3)
                sol(x+n//3, y, n//3)
                sol(x+n//3, y+n//3, n//3)
                sol(x+n//3, y+(n//3)*2, n//3)
                sol(x+(n//3)*2, y, n//3)
                sol(x+(n//3)*2, y+n//3, n//3)
                sol(x+(n//3)*2, y+(n//3)*2, n//3)
                return
    if col == -1:
        neg_cnt += 1
    elif col == 0:
        zero_cnt += 1
    else:
        pos_cnt += 1

sol(0, 0, n)
print(neg_cnt)
print(zero_cnt)
print(pos_cnt)
