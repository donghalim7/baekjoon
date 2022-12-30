case = int(input())

for i in range(case):
    test = input()
    score = 0
    point = 1
    for j in range(0, len(test)):
        if j == 0 and test[j] == "O":
            point = 1
        elif test[j] == "O":
            if test[j-1] == test[j]:
                point += 1
            else:
                point = 1
        else:
            continue
            
        
        if test[j] == "O":
            score += point
        else:
            continue
    
    print(score)