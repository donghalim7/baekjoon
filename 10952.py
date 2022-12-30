while True:
    num = input()
    

    if num == "0 0":
        break
    
    print(sum(list(map(int, num.split()))))