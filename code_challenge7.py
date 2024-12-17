def code_challenge7():
	didBuy = input("Did you buy a grocery (yes/ no): ")

	if didBuy.lower() == "yes" :
		nameItem = input("Name of the item: ")
		price = eval(input("Price of the item: "))
		age = eval(input("Age: "))
		givenAmount = eval(input("Amount Given: "))
	

		discount = round((price * 0.052), 2)
		discountPrice = round((price - discount), 2)
		tax = round((price * 0.123), 2)
		taxP = round((price + tax), 2)

		if age >= 60 :
			print(f"Hi consumer, you purchased a {nameItem}, with a price of {price}.php plus a 5.2% discount ({discount}php) to your total purchase.")
			print(f"Total of : {round((price - discount),2)}")
			print(f"Change : {round((givenAmount - discountPrice), 2)}")
			print("Thank you for shooping, please come again next time")
		elif age >=18 and age <= 59 :
			print(f"HI consumer, you purcahsed a {nameItem}, with a price of {price}.php plus a 12.3% tax ({tax}.php) to your total pruchase.")
			print(f"Total of : {round((price + tax ),2)}")
			print(f"Change : {round((givenAmount - taxP), 2)}")
			print("Thank you for shooping, please come again next time")

	else:
		print("Thank you for drooping by to our shop. See you next time.")

		