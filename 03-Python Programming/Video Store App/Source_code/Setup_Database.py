def setup_database():
    print("=======================================================")
    print("|                    VIDEO STORE                      |")
    print("|                 --SETUP DATABASE--                  |")
    print("=======================================================")
    print("| 1. Create Database/Schema Tables                    |")
    print("| 2. Insert Default Values                            |")
    print("| 3. Create Store Procedure                           |")
    print("=======================================================")
    print("| x. Exit                                             |")
    print("------------------------------------------------------|")
    choice = input("Choice: ")
    print("")
    print("")

    if (choice == "1"):
        from setup_database import Creating_Database_And_Tables

        setup_database()

    elif (choice == "2"):
        from setup_database import Insert_defualt_values

        setup_database()

    elif (choice == "3"):
        from setup_database import Create_Procedures
        setup_database()

    if ( (choice == "x") or (choice == "X") ):
        print("Exiting...")
        exit(0)

    else:
        print("")

setup_database()

        
