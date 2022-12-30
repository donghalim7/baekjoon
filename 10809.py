from string import ascii_lowercase

letter = input()

alphalist = list(ascii_lowercase)

for i in alphalist:
    if i in letter:
        print(letter.index(i), end=" ")
    else:
        print(-1, end=" ")