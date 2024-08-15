#=========================================================================
#Name: Sopumelela
#Surname: Sandekela
#Student Number: CON-1475940-C5L6
#Module: Python Programming
#Script name: Register_Customer.py
#Discription: This script is imported by the main program for registering 
#a customer. 
#=========================================================================


#=========================================================================
#FUNCTION: Go_insert_To_Database
#=========================================================================
def Go_insert_To_Database(num):

    class Customers(object):
        def __init__(self, fname, sname, address, phone):
            self.fname = fname
            self.sname = sname
            self.address = address
            self.phone = phone 

        def send_To_Server(self):
            from Application_Server_Side import insert_Customer
            insert_Customer(custInfo.fname, custInfo.sname, custInfo.address, custInfo.phone)
  
    def check_Null(info, count):

        def errorMessage():
            print("-------------------------------")
            print("Please enter the require info.")
            print("-------------------------------")
            print(" ")

        if count == 1:
            while info == '':
                errorMessage()
                info = input("Enter your First name: ")
            else:
                return info

        if count == 2:
            while info == '':
                errorMessage()
                info = value = input("Enter your surname: ")
            else:
                return info

        if count == 3:
            while info == '':
                errorMessage()
                info = input("Enter Email address: ")
            else:
                return info

            
    icount = 0
    arrCustInfo = []
    while icount != 3:
        icount += 1 

        if (icount == 1):
            value = input("Enter your First name: ")
            
            if value == '':
                value = check_Null(value, icount)

            arrCustInfo.append(value)

        elif (icount == 2):
            value = input("Enter your surname: ")

            if value == '':
                value = check_Null(value, icount)

            arrCustInfo.append(value)

        elif (icount == 3):
            value = input("Enter Email address: ")

            if value == '':
                value = check_Null(value, icount)

            arrCustInfo.append(value)
    
    custInfo = Customers( arrCustInfo[0], arrCustInfo[1], arrCustInfo[2], num)
    custInfo.send_To_Server()
#=========================================================================
   

    



#=========================================================================
#FUNCTION: get_feedBack
#=========================================================================
def get_feedback(feedback, number):
   
    if (feedback == 1):
        print(" ")
        print("------------------------------------------------------------")
        print("                WELCOME BACK TO VIDEO STORE                 ")
        print(" Your user account already exists no need to register again ")
        print("------------------------------------------------------------")
        print("<< Sending back to main menu <<...")
        print("------------------------------------------------------------")
        print(" ")
        print(" ")
        print(" ")
        
        from Main import client_Menu
        client_Menu()
    elif (feedback == 0):
        
        print(" ")
        print("------------------------------------------------------------")
        print("                        VIDEO STORE                         ")
        print("Phone number: ",number," is not of an existing account      ")
        print("------------------------------------------------------------")
        print(">> Submit the following required info for registration >>...")
        print("------------------------------------------------------------")
        print(" ")
        print(" ")

        Go_insert_To_Database(number)
#=========================================================================        



        


#=========================================================================
#FUNCTION: regCustomer
#=========================================================================
def regCustomer():
    print(" ")
    print(" ")
    print("=======================================================")
    print("|                    VIDEO STORE                      |")
    print("|                 REGISTER CUSTOMER                   |")
    print("=======================================================")
    print("| 1. Enter phone number                               |")
    print("| <. Return to main menu                              |")
    print("=======================================================")
    print("| x. Exit                                             |")
    print("-------------------------------------------------------")
    choice = str(input("Choice: "))
    print("-------------------------------------------------------")

    print(" ")
    print(" ")

    
    if ( choice == "1"):

        phoneNumber = str(input("Enter phone number: "))

        while (len(phoneNumber) != 10 ):

            if (phoneNumber == "<"):
                regCustomer()

            if ( (phoneNumber == "x") or (phoneNumber == "X") ):
                print("Exiting...")
                exit(0)

            print("-------------------------------------------------------")
            print("Incorrect input!")
            print("Remember: 10digit number with no spaces.")
            print("-------------------------------------------------------")
            print('Continue or enter "<" to go back to options|"x" to exit. ')
            print("-------------------------------------------------------")
            print(" ")

            phoneNumber = str(input("Enter phone number: "))
        else:
            print("-------------------------------------------------------")
            print("**********************VALIDATING***********************")
            print("-------------------------------------------------------")
            print(" ")
            
            return phoneNumber

    elif( choice == "<"):

        from Main import client_Menu
        client_Menu()
        
        
    elif ((choice == "x") or (choice == "X")):
        print("Exiting...")
        exit(0)




    