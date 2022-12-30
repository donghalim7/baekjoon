n, k = map(int, input().split())

def fac(i):
    mul = 1
    while i > 1:
        mul *= i
        i -= 1
    return mul

print(fac(n) // (fac(k) * fac(n - k)))