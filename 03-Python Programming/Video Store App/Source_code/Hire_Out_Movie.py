#=========================================================================
#Name: Sopumelela
#Surname: Sandekela
#Student Number: CON-1475940-C5L6
#Module: Python Programming
#Script name: Hire_Out_Movie.py
#Discription: This script is imported by the main program for hiring out 
#a movie. 
#=========================================================================

def Hire_Out_Movie():
    print(" ")
    print(" ")
    print("=======================================================")
    print("|                    VIDEO STORE                      |")
    print("|                 --HIRE OUT A MOVIE--                |")
    print("=======================================================")
    print("| 1. Enter Required info                              |")
    print("| <. Return to main menu                              |")
    print("=======================================================")
    print("| x. Exit                                             |")
    print("-------------------------------------------------------")
    choice = str(input("Choice: "))
    print("-------------------------------------------------------")
    print(" ")
    print(" ")


    def errorMessage():
        print("-------------------------------")
        print("Please enter the require info.")
        print("-------------------------------")
        print(" ")

    if (choice == '1'):
        icount = 0
        arrHireInfo = []
        while icount != 2:
            icount += 1

            if (icount == 1):
                number = input("Enter Your Phone number: ")
                while number == '':
                    errorMessage()
                    number = input("Enter Your Phone number: ")
                else:
                    arrHireInfo.append(number)
                    print("")


            elif (icount == 2):
                movieId = input("Enter the video ID of required movie: ")
                
                while (movieId == ''):
                    errorMessage()
                    movieId = input("Enter the video ID of required movie: ")
                else:
                    arrHireInfo.append(movieId)
                    return arrHireInfo

    elif (choice == "<"): 
        from Main import client_Menu
        client_Menu() 

    elif ( (choice == "x") or (choice == "X") ):
        exit(0)
        print("Exiting....")

    else:
        errorMessage()
        Hire_Out_Movie()