def code_challenge14():
    sum = True
    n1 = 0

    while sum == True:
        next = eval(input("Please enter a number ---> "))

        if next == 0 :
            print(f"The sum of all the numbers is {n1}")
            print("LOOP TERMINATED")
            break
        else:
            print("Please continue entering a number")
            n1 += next
            continue
