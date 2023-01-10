import sys

m = int(sys.stdin.readline())
s = set()


for _ in range(m):
    cmd = sys.stdin.readline().split()
    if len(cmd) != 1:
        cmd[1] = int(cmd[1])

    if cmd[0] == "add":
        if cmd[1] not in s:
            s.add(cmd[1])
        else:
            continue
        
    elif cmd[0] == "remove":
        if cmd[1] in s:
            s.remove(cmd[1])
        else:
            continue
    
    elif cmd[0] == "check":
        if cmd[1] in s:
            print(1)
        else:
            print(0)

    elif cmd[0] == "toggle":
        if cmd[1] in s:
            s.remove(cmd[1])
        else:
            s.add(cmd[1])

    elif cmd[0] == "all":
        s.clear()
        s.update(i for i in range(1, 21))

    else:
        s.clear()
    