def code_challenge12():
    for a in range(1,6):
        for b in range(6, a, -1):
            print(" ", end=" ")
        for c in range(1, a+1):
            print("*", end=" ")
        for d in range(1, a):
            print("*", end=" ")  
        print()      

    for x in range(1, 5):
        print("", end=" ")
        for y in range(1, 5):
            print(" ",end=" ")
        for z in range(1,3):
            print("*", end=" ")
        print()          