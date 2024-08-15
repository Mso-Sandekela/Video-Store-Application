#=========================================================================
#Name: Sopumelela
#Surname: Sandekela
#Student Number: CON-1475940-C5L6
#Module: Python Programming
#Discription: This script is the main script that the user initially interacts with 
#=========================================================================


#---------------------------------------------------------------------------------
#Customers main menu...
#---------------------------------------------------------------------------------
def client_Menu():
    print("=======================================================")
    print("|                    VIDEO STORE                      |")
    print("=======================================================")
    print("| 1. Register Customer                                |")
    print("| 2. Register Movie                                   |")
    print("=======================================================")
    print("| 3. Hire Out Movie                                   |")
    print("| 4. Return Movie                                     |")
    print("=======================================================")
    print("| 5. About / How to use                               |")
    print("=======================================================")
    print("| x. Exit                                             |")
    print("------------------------------------------------------|")
    choice = input("Choice: ")

#If Register Customer is choosed.
    if   ( choice == "1"):

        #Receive phoneNumber from the Register_Customer module.
        from Register_Customer import regCustomer
        phoneNumber = regCustomer()


        #Pushing the phone number to the Application_Server_Side...
        from Application_Server_Side import regCustomer_Check_If_Exists
        regCustomer_Check_If_Exists(phoneNumber)

#If Register Movie is choosed.
    elif ( choice == "2"):
        from Register_Movie import regMovie
        arrMovie = regMovie()
 
        from Application_Server_Side import register_Movie_Check, add_Ver_Or_Insert
        found = register_Movie_Check(arrMovie[0])
        
        message = add_Ver_Or_Insert(found, arrMovie[0], arrMovie[1])

        print(" ")
        print("**************************************************")
        print(message)
        print("**************************************************")
        print(" ")
        print(" ")
        client_Menu()


#If Hire Out Movie is choosed.
    elif ( choice == "3"):
        from Hire_Out_Movie import Hire_Out_Movie
        arrHireOut = Hire_Out_Movie()

        from Application_Server_Side import Hire_Out_Movie
        message = Hire_Out_Movie(arrHireOut[0], arrHireOut[1])
        
        print(" ")
        print("**************************************************")
        print(message)
        print("**************************************************")
        print(" ")
        print(" ")
        client_Menu()

    elif ( choice == "4"):

        from Return_Movie import ReturnMovieMenu
        id = ReturnMovieMenu()

        from Application_Server_Side import return_Movie
        message = return_Movie(id)
        
        print(" ")
        print("**************************************************")
        print(message)
        print("**************************************************")
        print(" ")
        print(" ")
        client_Menu()

    elif ( choice == "5"):
        print("")
        print("")
        f = open("About.txt", "r")
        print(f.read())
        print("")
        print("")
        print("")
        client_Menu()

    elif ((choice  == "x") or (choice == "X")):
        print("Exiting...")
        exit(0)
        
        

client_Menu()
#=========================================================================
#Main script Completed successfully...
#=========================================================================
