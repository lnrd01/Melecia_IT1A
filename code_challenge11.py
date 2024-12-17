def code_challenge11():
    for e in range(1, 8):
        for d in range(7, e, -1):
            print(" ", end=" ")
        for c in range(1, e+1):
            print("*", end=" ")
        for b in range(1, e):
            print("*", end=" ")    
        print()
    for x in range(1, 7):
        for y in range(1, x+1):
            print(" ", end=" ")
        for z in range(7, x+1, -1):
            print("*", end=" ")
        for a in range(7, x, -1):
            print("*", end=" ")    
        print() 