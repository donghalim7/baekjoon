def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1


n = int(input())

num = str(factorial(n))
num = num[::-1]
zero = 0

for i in num:
    if i == "0":
        zero += 1
    else:
        break

print(zero)