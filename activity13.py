def act13():
    #for loop with range
    factorial = 1
    number = eval(input("Enter a Number : "))
    for i in range(number, 0, -1): #implementation of stopping point (function to increment or decrement)
        #factorial
        factorial *= i
        print(factorial)
