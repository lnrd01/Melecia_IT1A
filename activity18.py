def act18():
    triangles = eval(input("Enter number of Triangles : "))

    for x in range(1, 8):
        for y in range(triangles):
            for a in range(1, x+1):
                print("*", end=" ")
            for b in range(7, x, -1):
                print(" ", end=" ")
            print(" ", end=" ")
        print()
