from activity1 import act1
from activity2 import act2
from activity3 import act3
from activity4 import act4
from activity5 import act5
from activity6 import act6
from activity7 import act7
from activity8 import act8
from activity9 import act9
from activity10 import act10
from activity11 import act11
from activity12 import act12
from activity13 import act13
from activity14 import act14
from activity15 import act15
from activity16 import act16
from activity17 import act17
from activity18 import act18
from activity19 import act19
from activity20 import act20
from activity21 import act21
from activity22 import act22
from activity23 import act23
from activity24 import act24
from activity25 import act25

from code_challenge1 import code_challenge1
from code_challenge2 import code_challenge2
from code_challenge3 import code_challenge3
from code_challenge4 import code_challenge4
from code_challenge5 import code_challenge5
from code_challenge6 import code_challenge6
from code_challenge7 import code_challenge7
from code_challenge8 import code_challenge8
from code_challenge9 import code_challenge9
from code_challenge10 import code_challenge10
from code_challenge11 import code_challenge11
from code_challenge12 import code_challenge12
from code_challenge13 import code_challenge13
from code_challenge14 import code_challenge14
from code_challenge15 import code_challenge15
from code_challenge16 import code_challenge16
import os
def finals():
    fun = True
    name = input("Please enter your name: ")
    while fun :
        os. system('cls')
        print(f"Hello {name}, welcome to my program. \n============================ \n\t[Main Menu]: \n1.Activities \n2.Code Challenges \n3.Exit")
        print("============================")
        choose = input("Please choose a number: ")
        if  choose == "1":
            idk = True
            while idk:
                next1 = input("============================================== \n[Activity Section] \nChoose an activity from 1-25 (Enter 0 to exit) \n============================================== \nEnter a number: ")
                if next1 == "1":
                    print("This is my activity no.1")
                    act1()
                elif next1 == "2":
                    print("This is my activity no.2")
                    act2()
                elif next1 == "3":
                    print("This is my activity no.3")
                    act3()
                elif next1 == "4":
                    print("This is my activity no.4")
                    act4()
                elif next1 == "5":
                    print("This is my activity no.5")
                    act5()
                elif next1 == "6":
                    print("This is my activity no.6")
                    act6()
                elif next1 == "7":
                    print("This is my activity no.7")
                    act7()
                elif next1 == "8":
                    print("This is my activity no.8")
                    act8()
                elif next1 == "9":
                    print("This is my activity no.9")
                    act9()
                elif next1 == "10":
                    print("This is my activity no.10")
                    act10()
                elif next1 == "11":
                    print("This is my activity no.11")
                    act11()
                elif next1 == "12":
                    print("This is my activity no.12")
                    act12()
                elif next1 == "13":
                    print("This is my activity no.13")
                    act13()
                elif next1 == "14":
                    print("This is my activity no.14")
                    act14()
                elif next1 == "15":
                    print("This is my activity no.15")
                    act15()
                elif next1 == "16":
                    print("This is my activity no.16")
                    act16()
                elif next1 == "17":
                    print("This is my activity no.17")
                    act17()
                elif next1 == "18":
                    print("This is my activity no.18")
                    act18()
                elif next1 == "19":
                    print("This is my activity no.19")
                    act19()
                elif next1 == "20":
                    print("This is my activity no.20")
                    act20()
                elif next1 == "21":
                    print("This is my activity no.21")
                    act21()
                elif next1 == "22":
                    print("This is my activity no.22")
                    act22()
                elif next1 == "23":
                    print("This is my activity no.23")
                    act23()
                elif next1 == "24":
                    print("This is my activity no.24")
                    act24()
                elif next1 == "25":
                    print("This is my activity no.25")
                    act25()
                elif next1 == "0":
                    break
                else:
                    print("Invalid number please try again.")
                    continue
        
        elif choose == "2":
            con = True
            while con:
                choose2 = input("================================================================ \n[Code Challenges]: \nPlease pick a number of the code challenge 1-16(Enter 0 to exit) \n================================================================ \nEnter a number: ")

                if choose2 == "1":
                    print("This is my code challenge no.1")
                    code_challenge1()
                elif choose2 == "2":
                    print("This is my code challenge no.2")
                    code_challenge2()
                elif choose2 == "3":
                    print("This is my code challenge no.3")
                    code_challenge3()
                elif choose2 == "4":
                    print("This is my code challenge no.4")
                    code_challenge4()
                elif choose2 == "5":
                    print("This is my code challenge no.5")
                    code_challenge5()
                elif choose2 == "6":
                    print("This is my code challenge no.6")
                    code_challenge6()
                elif choose2 == "7":
                    print("This is my code challenge no.7")
                    code_challenge7()
                elif choose2 == "8":
                    print("This is my code challenge no.8")
                    code_challenge8()
                elif choose2 == "9":
                    print("This is my code challenge no.9")
                    code_challenge9()
                elif choose2 == "10":
                    print("This is my code challenge no.10")
                    code_challenge10()
                elif choose2 == "11":
                    print("This is my code challenge no.2")
                    code_challenge11()
                elif choose2 == "12":
                    print("This is my code challenge no.2")
                    code_challenge12()
                elif choose2 == "13":
                    print("This is my code challenge no.2")
                    code_challenge13()
                elif choose2 == "14":
                    print("This is my code challenge no.2")
                    code_challenge14()
                elif choose2 == "15":
                    print("This is my code challenge no.2")
                    code_challenge15()
                elif choose2 == "16":
                    print("This is my code challenge no.2")
                    code_challenge16()
                    pass
                elif choose2 == "0":
                    break
                else:
                    print("Invalid syntax please try again")
                    continue


        elif choose == "3":
                print("Program terminated")
                break
        else:
            print("Invalid number please try again.")
            continue

finals()
