def act25():
    #list
    courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

    courses.remove("Delete w/o index")
    courses.pop()
    courses.append("DHRS")
    courses.insert(0, "ABELS")

    print(courses)

    #i check w3schools for the methods in list, theres a lot i know but i think this will be mostly used 
