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