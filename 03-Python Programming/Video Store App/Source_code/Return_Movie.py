#=========================================================================
#Name: Sopumelela
#Surname: Sandekela
#Student Number: CON-1475940-C5L6
#Module: Python Programming
#Script name: Return_Movie.py
#Discription: This script is imported by the main program for returning 
#hiring out movies. 
#=========================================================================

def ReturnMovieMenu():
    print(" ")
    print(" ")
    print("=======================================================")
    print("|                    VIDEO STORE                      |")
    print("|                  --RETURN MOVIE--                   |")
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
        videoId = input("Enter Video Id: ")
        while videoId == '':
            errorMessage()
            videoId = input("Enter Video Id: ")
        else:
            print("")
            return videoId


    elif (choice == "<"): 
        from Main import client_Menu
        client_Menu() 

    elif ( (choice == "x") or (choice == "X") ):
        exit(0)
        print("Exiting....")

    else:
        errorMessage()
        ReturnMovieMenu()