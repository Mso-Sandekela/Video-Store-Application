#=========================================================================
#Name: Sopumelela
#Surname: Sandekela
#Student Number: CON-1475940-C5L6
#Module: Python Programming
#Script name: Application_Server_Side.py
#Discription: This script is server side that 
#communicates with all of the Users interactions. 
#=========================================================================

#=========================================================================
#FUNCTION: Hire_Out_Movie
#=========================================================================
def return_Movie(id):
    import mysql.connector
    from mysql.connector import errorcode

    try:
        conn = mysql.connector.connect(
            user = "root",
            passwd = "123456",
            host = "localhost",
            database = "video_store")
        
        query = f"""UPDATE hire
            SET dateReturn = current_date() 
            WHERE videoId = {id}
        """

        cur = conn.cursor()
        cur.execute(query)
        conn.commit()

        message = "Hired movie sucessfully Returned."

        return message
        
        cur.close()
        conn.close()  
 
  

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect user name or password!")

        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exits.")

        else:
            print(err)
#=========================================================================


#=========================================================================
#FUNCTION: Hire_Out_Movie
#=========================================================================
def Hire_Out_Movie(phoneNumber, vidId):
    import mysql.connector
    from mysql.connector import errorcode

    try:
        conn = mysql.connector.connect(
            user = "root",
            passwd = "123456",
            host = "localhost",
            database = "video_store")
        

        call_sp_HireOutMovie = "call sp_HireOutMovie('"
        call_sp_HireOutMovie += phoneNumber + "' , "
        call_sp_HireOutMovie += str(vidId)
        call_sp_HireOutMovie += ");"


        cur = conn.cursor()
        cur.execute(call_sp_HireOutMovie)
        conn.commit()

        message = "Movie sucessfully hired out."

        return message
        
        cur.close()
        conn.close()  
 
  

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect user name or password!")

        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exits.")

        else:
            print(err)
#=========================================================================



#=========================================================================
#FUNCTION: add_Ver_Or_Insert
#=========================================================================
def add_Ver_Or_Insert(found, name, type):
    import time
    import mysql.connector
    from mysql.connector import errorcode
    
    #Use the time tuple from the time module to constract 
    #a data format suitable for MYSQL
    timeTuple = time.gmtime()
              #           YEAR                    MONTH                    DAY
    current_time = str(timeTuple[0]) +"-"+ str(timeTuple[1]) +"-"+ str(timeTuple[2])
 

    try:

        conn = mysql.connector.connect(user = "root",
                                       passwd = "123456",
                                       host = "localhost",
                                       database = "video_store")
        
        #If movie name not found on the database a new movie is registered.
        if (found == 0 ):
            cur = conn.cursor()
            query = f"""INSERT INTO video (videoVer, vName, type, dateAdded) 
            VALUES (1,'{name}', '{type}', '{current_time}'); """
            cur.execute(query)
            conn.commit()
            message = "New movie has been registered to the database."
            
        
        #If movie name exists on the database the movie version is increased.
        elif (found == 1 ):
            cur = conn.cursor()
            query = f""" UPDATE video
            SET videoVer = videoVer + 1 
            WHERE vName = '{name}';
            """
            cur.execute(query)
            conn.commit()
            message = f"Movie: {name} exists, Video version has been added for {name}."

        
        #Turn message to the Main menu page. 
        return message

        
        cur.close()    
        conn.close()

    except mysql.connector.Error as err:
        if (err.errno == errorcode.ER_ACCESS_DENIED_ERROR):
            print("Incorrect user name or password!")

        elif (err.errno == errorcode.ER_BAD_DB_ERROR):
            print("Database does not exist.")
        else:
            print(err)
#=========================================================================

#=========================================================================
#FUNCTION: register_Movie_Check
#=========================================================================
def register_Movie_Check(name):
    import mysql.connector
    from mysql.connector import errorcode
    

    try:
        conn = mysql.connector.connect(user = "root",
                                       passwd = "123456",
                                       host = "localhost",
                                       database = "video_store")

        cur = conn.cursor()

        query = "call sp_Check_MovieExists('"
        query += name 
        query += "');"

        cur.execute(query)

        bFound = cur.fetchone()[0] 

        return bFound
        
        cur.close()
        conn.close()

        

    except mysql.connector.Error as err:
        if (err.errno == errorcode.ER_ACCESS_DENIED_ERROR):
            print("Incorrect user name or password!")

        elif (err.errno == errorcode.ER_BAD_DB_ERROR):
            print("Database does not exist.")
        else:
            print(err)

#=========================================================================


#=========================================================================
#FUNCTION: insert_Customer
#=========================================================================
def insert_Customer(fName, sName, sAddress, sPhone):
    import mysql.connector
    from mysql.connector import errorcode

    try:
        conn = mysql.connector.connect(
            user = "root",
            passwd = "123456",
            host = "localhost",
            database = "video_store")

        call1 = "call sp_Insert_Customer( "
        customerInfo = " '"+fName+"', '"+sName+"', '"+sAddress+"', '"+sPhone+"' "
        call2 = ");"
        
        sp_Insert_Customer = call1 + customerInfo + call2

        cur = conn.cursor()

        cur.execute(sp_Insert_Customer)
        conn.commit()
        
        print("")
        print("******************************************")
        print("Customer successfully added...")
        print("******************************************")
        print("")
        print("")
        print("")

        from Main import client_Menu
        client_Menu()
    
        cur.close()
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect user name or password!")

        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exits.")

        else:
            print(err)
#=========================================================================


#=========================================================================
#FUNCTION: regCustomer_Check_If_Exists
#=========================================================================
def regCustomer_Check_If_Exists(number):
    import mysql.connector
    from mysql.connector import errorcode

    try:
        conn = mysql.connector.connect(
            user = "root",
            passwd = "123456",
            host = "localhost",
            database = "video_store")

    #import phoneNumber from Register_Customer after being received from user.
    #To be used to check whether user exist on the Customer database.
    #from Register_Customer import phoneNumber         

        call1 = "call sp_Check_ClientExists('"
        call2 = "');"


    # "call sp_Check_ClientExists(' +phonenumber+ ')"
        call_sp_Check_ClientExists = call1 +  number + call2

        cur = conn.cursor()
        cur.execute(call_sp_Check_ClientExists)

        bFound = cur.fetchone()[0]

        
        cur.close()
        conn.close()
        
  
        #Sends the feedback to a function on the register customer modules.   
        from Register_Customer import get_feedback    
        get_feedback(bFound, number)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect user name or password!")

        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exits.")

        else:
            print(err)
#=========================================================================








    
        

