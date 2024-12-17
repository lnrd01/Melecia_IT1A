name = input("Enter your name: ")
amount = eval(input("Enter your deposit amount: "))

thousand = amount // 1000
s1 = amount % 1000
five_h= s1 // 500
s2 = s1 % 500
two_h = s2 // 200
s3 = s2 % 200
one_h = s3 // 100
s4 = s3 % 100
fifty = s4 // 50
s5 = s4 % 50
twenty = s5 // 20
s6 = s5 % 20
ten = s6 // 10
s7 = s6 % 10
five = s7 // 5
s8 = s7 % 5
one = s8 // 1   

print("Hello,",name)
print("The amount you deposit is distributed in PH denomination as follows: ")
print("--------------------------------------------------------------------")
print(thousand, " -1000")
print(five_h, " -500")
print(two_h, " -200")
print(one_h, " -100")
print(fifty, " -50")
print(twenty, " -20")
print(ten, " -10")
print(five, " -5")
print(one, " -1")