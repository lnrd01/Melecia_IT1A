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