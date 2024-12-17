def act19():
    ben = True
    while ben == True:
        name = input("Enter a name: ")
        
        if name.lower() == "stop":
            print("The loop has been termninated")
            
            break
            ben = False
