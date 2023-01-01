T = int(input())

for i in range(T):
    data = list(input())
    count = []

    if data[0] == ")":
        print("NO")
    
    else:
        for j in range(1, len(data)):
            if (data[j] == data[j-1]) and data[j] == "(":
                count.append(1)
            elif (data[j] == data[j-1]) and data[j] == ")":
                count.append(-1)
        
        if len(count) == 0:
            print("NO")
        elif count[0] == -1:
            print("NO")
        elif sum(count) == 0:
            print("YES")
        elif sum(count) != 0:
            print("NO")