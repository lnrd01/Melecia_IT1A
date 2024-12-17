def code_challenge6():
	prelim = eval(input("Enter your grades in prelim: "))
	midterm = eval(input("Enter your grades in midterm: "))
	semi_finals = eval(input("Enter your grades in semi-finals: "))
	finals = eval(input("Enter your grades in finals: "))
	quiz = eval(input("Enter your grades in quiz: "))
	project = eval(input("Enter your grades in project: "))


	if (prelim >= 65 and prelim <=100) and (midterm >= 65 and midterm <=100) and (semi_finals >= 65 and semi_finals <=100) and (finals >= 65 and finals <=100) and (quiz >= 65 and quiz <=100) and (project >= 65 and project <=100) :
		fg = (prelim * .15) + (midterm * .15) + (semi_finals * .15) + (finals * .15) + (quiz * .25) + (project * .15)
		#Nested Condition
		if fg >= 75 :
			print("Congratulations, you passed the course")


		else :
			print("Sorry, you failed the course")

	else :
		print("INVALID GRADES")

	print("PROGRAM END")