while True:
    x, y, z = map(int, input().split())


    if x == 0 and y == 0 and z == 0:
        break

        
    if max(x, y, z) == x:
        if x ** 2 == y ** 2 + z ** 2:
            print("right")
        else:
            print("wrong")

    elif max(x, y, z) == y:
        if y ** 2 == x ** 2 + z ** 2:
            print("right")
        else:
            print("wrong")

    elif max(x, y, z) == z:
        if z ** 2 == x ** 2 + y ** 2:
            print("right")
        else:
            print("wrong")