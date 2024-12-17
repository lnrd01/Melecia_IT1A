#The summation of 10 numbers
def code_challenge8():
    num1 = 0

    for i in range(1, 11):
        num2 = eval(input(f"Enter a number {i}: "))
        num1 += num2

    print(f"The summation of all 10 numbers is {num1}")