#=========================================================================
#Name: Sopumelela
#Surname: Sandekela
#Student Number: CON-1475940-C5L6
#Module: Python Programming
#Script name: Register_Movie.py
#Discription: This script is imported by the main program for registering 
#a customer. 
#=========================================================================


#=========================================================================
#FUNCTION: regMovie
#=========================================================================
def regMovie():
    print(" ")

    print(" ")
    print("=======================================================")
    print("|                    VIDEO STORE                      |")
    print("|                   REGISTER MOVIE                    |")
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
        arrMovieInfo = []
        while icount != 2:
            icount += 1

            if (icount == 1):
                movieName = input("Enter movie name: ")
                while movieName == '':
                    errorMessage()
                    movieName = input("Enter movie name: ")
                else:
                    arrMovieInfo.append(movieName)
                    print("")

            elif (icount == 2):
                print("--------------------------------------------------")
                print("REMEMBER: 'R' for new movies & 'B' for old movies.")
                print("--------------------------------------------------")
                movieType = input("Enter movie type: ")
                

                while (movieType == '') or (len(movieType) > 1):
                    errorMessage()
                    movieType = input("Enter movie type: ")
                else:
                    arrMovieInfo.append(movieType)
                    return arrMovieInfo

    elif (choice == "<"): 
        from Main import client_Menu
        client_Menu() 

    elif ( (choice == "x") or (choice == "X") ):
        exit(0)
        print("Exiting....")

    else:
        errorMessage()
        regMovie()
#=========================================================================





