a, b = input().split()

aRev = a[::-1]
bRev = b[::-1]

print(max(int(aRev), int(bRev)))