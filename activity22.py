def act22():
    def act1():
        print("Hello World")

    def act3():
        Name = input("Enter your full name: ")
        Age = input("Enter your age: ")
        Gender = input("Enter your gender: ")
        DOB = input("Enter your date of birth: ")
        Address = input("Enter your address: ")
        CPN = input("Enter your cellphone number: ")
        EmailAdd = input("Enter your email address: ")
        MothersName = input("Enter your mother's name: ")
        FathersName = input("Enter your father's Name: ")
        MaritalStatus = input("Enter your marital status: ")
        Religion = input("Enter your religion: ")
        Language = input("Enter your language learn: ")

        print("Hello, my name is", Name , "a", Age , "year-old born on", DOB , "and lives in", Address ,". My parents are", MothersName , "and", FathersName, ". I'm", Gender ,"and my religion is", Religion , "and speaks", Language,". You can contact me in my cellphone number", CPN , "or to my email address ",EmailAdd ,"for more information.")

    def act4():
        num1 = eval(input("Enter a number : "))
        num2 = eval(input("Enter another number : "))
        answer = num1 + num2
        print("The sum of ", num1, " + ", num2,  " is ", answer,".")

    def act5():
        print("FAHRENHEIT TO CELSIUS CONVERTER PROGRAM")

        print("=======================================")

        fahrenheit = eval(input("Enter temperature in fahrenheit ---> : "))

        celsuis = ((fahrenheit - 32) * 5) / 9

        print( fahrenheit, "degrees fahrenheit converted to celsuis is" , celsuis, "degrees")

        print(f" {fahrenheit}degrees fahrenheit converted to celsuis is {celsuis} degrees")

        print(round(celsuis, 2))

        print(f" {fahrenheit} degrees fahrenheit converted to celsuis is {round(celsuis, 2)} degrees")

    def act6():
#Assignment Operator Activity
        x = 5 

        print(x)

        x = x + 10

        print (x)

        x = x + 15

        print(x)

        x += 10

        print(x)

#Introduction to Conditional Statements
    def act7():

        gold = 0

        miner = input("Hi, what is your name: ")

        isGold = input("Is the mineral gold? ")

        if isGold.lower() == "yes":
            gold += 1
            print(f"Hi {miner}, your total number of gold is {gold}")

        else:
            print(f"Hi {miner}, your total number of gold is {gold}")

    def act8():
        password = input("PASSWORD : ")
        if password == "secret":
            print("Successfully Logged in")
            print("System finished")
        elif password == "hatdog":
            print("Cheesedog Logged in")
        else:
            print("Incorrect password please try again...")

    def act9():
        user = input("ENTER NAME : ")
        age = eval(input("ENTER AGE : "))

        if age >= 1 and age <= 7:
            print(f"Hi {user}, you are toddler.")
        elif age >= 8 and age <= 13:
            print(f"Hi {user}, you are pre teen.")
        elif age >= 14 and age <= 18:
            print(f"Hi {user}, you are teenager.")
        elif age >= 19 and age <= 31:
            print(f"Hi {user}, you are early adulthood.")
        elif age >= 32 and age <= 45:
            print(f"Hi {user}, you are mid adulthood.")
        elif age >= 46 and age <= 59:
            print(f"Hi {user}, you are post adulthood.")
        elif age >= 60 and age <= 100:
            print(f"Hi {user}, you are senior.")
        else:
            print(f"Impossible Your Alive, {user}!")

    def act10():
        name = input("Enter your name : ")
        isStudent = input("Are yur a current student of DLL (yes/no) : ")
        if isStudent.lower() == "yes":
            yearLevel = input("What year are you currently enrolled ? \nF - Freshmen \nS - Sophamore\nJ - Junior\nR - Senior : \nPlease Input your answer here : ")
        if yearLevel.lower() == "f":
            print(f"Hi {name}, Freshmen, Welcome to DLL ")
        elif yearLevel.lower() == "s":
            print(f"Hi {name}, Sophamore, Welcome to DLL ")
        elif yearLevel.lower() == "j":
            print(f"Hi {name}, Junior, Welcome to DLL ")
        elif yearLevel.lower() == "r":
            print(f"Hi {name}, Senior, Welcome to DLL ")
        else:
            print("Thank you for using the program ")
		
    def act11():
        for circle in range(1, 11):
            print("I am Lenard")

#implementation of stopping point (function to increment or decrement)
        
    def act12():
        for now in range(10, 0, -1):
            print(now)
		
    def act13():
        #for loop with range
        factorial = 1
        number = eval(input("Enter a Number : "))
        for i in range(number, 0, -1): #implementation of stopping point (function to increment or decrement)
        #factorial
            factorial *= i
            print(factorial)

    def act14():
        #for loop complete range
        for i in range(0 , 11): 
            print(i, end = " ")
            for y in range(0, 11):
                print("*", end = " ")
            print()

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

    def act16():
    #for loop complete range
        for x in range(1 , 6): 
            for y in range(1, x + 1):
                print(" ", end = " ")
            for z in range (6, x , -1):
                print("*",end = " ")
            print()

    def act17():
        columns = eval(input("Enter number of Columns : "))

        for x in range(1,11): 
            for y in range(1, columns + 1):
                print(f"{x} x {y} = {x * y}", end ="\t")
            print()

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

    def act19():
        ben = True
        while ben == True:
            name = input("Enter a name: ")
        
            if name.lower() == "stop":
                print("The loop has been termninated")
                break
                ben = False

    def act20():
        import os
        isContinue = True
        nt = 0
        while isContinue == True:
            ask = input("Do you like to create more triangle (yes / no): ")
            if ask.lower() == "no":
                print("Program Terminated")
                break
                isContinue = False
            
            elif ask.lower() == "yes":
                os.system('cls')
                nt += 1
                for x in range(1,5):
                    for r in range(1, nt + 1):
                        for y in range(1, x + 1):
                            print("*", end = " ")
                        for z in range(5, x, -1):
                            print(" ", end = " ")
                        print(end="")
                    print()
                continue
            else:
                print("Invalid answer, please only answer in 'yes' or 'no'")
                continue
    
    

    isContinue = True
    while isContinue:
        ask = input("Select the python file you want to open : \n1.) activity4 \n2.) activity6 \n3.) activity7 \n4.) activity8 \n5.) exit \nInput : ")
        if ask == "1":
            print("Program is running")
            act4()
        elif ask == "2":
            print("Program is running")
            act6()
        elif ask == "3":
            print("Program is running")
            act7()
        elif ask == "4":
            print("Program is running")
            act8()
        elif ask == "5":
            break
        else:
            continue

