def code_challenge9():
    for x in range(1, 7):
        for y in range(1, x):
            print(" ", end=" ")
        for z in range(7, x, -1):
            print("*", end=" ")
        print()    