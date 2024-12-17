def code_challenge13():
    for e in range(1, 6):
        for d in range(6, e, -1):
            print(" ", end=" ")
        for c in range(e, 1, -1):
            print(c, end=" ")
        for b in range(1, e+1):
            print(b, end=" ")    
        print()

    for x in range(4, 0, -1):
        for y in range(6, x, -1):
            print(" ", end=" ")
        for z in range(x, 0, -1):
            print(z, end=" ")
        for a in range(2, x+1):
            print(a, end=" ")          
        print() 
