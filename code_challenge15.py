#Hybrid Loop
def code_challenge15():
    go = True
    no = 0

    while go:
        may = input("Do you wish to create a new triangle (yes or no): ")

        if may.lower() == "no":
            print("LOOP TERMINATED")
            break

        elif may.lower() == "yes":
            no += 1
            for x in range(1, 6):
                for r in range(1, no + 1):
                    for y in range(1, x + 1):
                        print("*", end = " ")
                    for z in range(6, x, -1):
                        print(" ", end = " ")
                print("\t")
            continue
        else:
            print("Invalid answer, please only type 'yes' or 'no' ")
            continue

