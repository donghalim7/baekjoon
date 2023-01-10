import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

pokemon = dict()
num = 1

for _ in range(n):
    name = sys.stdin.readline().rstrip()
    dict[num] = name

pokemon_rev = {v:k for k, v in pokemon.items()}

quiz = []

for _ in range(m):
    ip = sys.stdin.readline().rstrip()

    if ip.isdigit() == True:
        ip = int(ip)

        print(pokemon[ip])

    else:
        print(pokemon_rev[ip])
