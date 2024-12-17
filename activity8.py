def act8():
	password = input("PASSWORD : ")

	if password == "secret":
		print("Successfully Logged in")
		print("System finished")
	elif password == "hatdog":
		print("Cheesedog Logged in")
	else:
		print("Incorrect password please try again...")