def act15():
    #for loop complete range
    for i in range(0 , 11): 
        print(i, end = " ")
        for y in range(0, i):
            print("*", end = " ")
        print()
        
    for i in reversed(range(0 , 12)): 
        print(i, end = " ")
        for y in range(0, i):
            print("*", end = " ")
        print()
