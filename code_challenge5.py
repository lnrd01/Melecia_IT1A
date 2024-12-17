def code_challenge5():
    print("FAHRENHEIT TO CELSIUS CONVERTER PROGRAM")

    print("=======================================")

    fahrenheit = eval(input("Enter temperature in fahrenheit ---> : "))

    celsuis = ((fahrenheit - 32) * 5) / 9

    print( fahrenheit, "degrees fahrenheit converted to celsuis is" , celsuis, "degrees")

    print(f" {fahrenheit}degrees fahrenheit converted to celsuis is {celsuis} degrees")

    print(round(celsuis, 2))

    print(f" {fahrenheit} degrees fahrenheit converted to celsuis is {round(celsuis, 2)} degrees")
