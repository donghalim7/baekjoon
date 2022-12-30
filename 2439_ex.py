# n = int(input())
# for i in range(1, n+1):
# 	print(' '*(n-i) + '*'*i)

n = int(input())
for i in range(n):						
    star = "*"*(i+1)
    print(star.rjust(n))