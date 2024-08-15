#=========================================================================
#Name: Sopumelela
#Surname: Sandekela
#Student Number: CON-1475940-C5L6
#Module: Python Programming
#Script name: Application_Server_Side.py
#Discription: This module is a module for creating Stored procedures that
#the Application_Server_Side.py module will communicate with.
#=========================================================================

import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(
        user="root", 
        passwd="123456", 
        host="localhost", 
        database="video_store")

#=========================================================================
#PROCEDURE: sp_Check_ClientExists
#=========================================================================
    cur = conn.cursor()
    create_sp_query = """
        CREATE PROCEDURE sp_Check_ClientExists(IN num VARCHAR(10))
        BEGIN
            DECLARE i INT;
            DECLARE bFound BOOL;

            SELECT COUNT(phone) INTO i FROM customers WHERE phone = num;

            IF i = 0 THEN
                SET bFound = FALSE;
            ELSE
                SET bFound = TRUE;
            END IF;

            SELECT bFound;

        END;
    """

    cur.execute("DROP PROCEDURE IF EXISTS sp_Check_ClientExists;")

    cur.execute(create_sp_query)

    print("STORED PROCEDURE: sp_Check_ClientExists CREATED...")
    print(" ")
#=========================================================================


#=========================================================================
#PROCEDURE: sp_Insert_Customer
#=========================================================================
    cur = conn.cursor()

    create_sp_query = """
        CREATE PROCEDURE sp_Insert_Customer(
        IN firstName VARCHAR(40),
        IN surname VARCHAR(40),
        IN email VARCHAR(40),
        IN number VARCHAR(10))
        BEGIN

            INSERT INTO customers (fname, sname, address, phone)
            VALUES (firstName, surname, email, number);

        END
    """
    cur.execute("DROP PROCEDURE IF EXISTS sp_Insert_Customer;")

    cur.execute(create_sp_query)
    print("STORED PROCEDURE: sp_Insert_Customer CREATED...")
    print(" ")


#=========================================================================
 
#=========================================================================
#PROCEDURE: sp_Insert_Customer
#=========================================================================
    cur = conn.cursor()

    create_sp_query = """
        CREATE PROCEDURE sp_Check_MovieExists(IN movie VARCHAR(40))
        BEGIN
            DECLARE i INT;
            DECLARE bFound BOOL;

            SELECT COUNT(vName) INTO i FROM video WHERE vName = movie;

            IF i = 0 THEN
                SET bFound = FALSE;
            ELSE
                SET bFound = TRUE;
            END IF;

            SELECT bFound;

        END;
    """

    cur.execute("DROP PROCEDURE IF EXISTS sp_Check_MovieExists;")

    cur.execute(create_sp_query)
    conn.commit()

    print("STORED PROCEDURE: sp_Check_MovieExists CREATED...")
    print(" ")
#=========================================================================

#=========================================================================
#PROCEDURE: sp_HireOutMovie
#=========================================================================
    cur = conn.cursor()

    create_sp_query = """
        CREATE PROCEDURE sp_HireOutMovie(IN num VARCHAR(10),
								         IN vidID INT)
        BEGIN
            DECLARE id INT;
            DECLARE ver INT;

            SELECT custID INTO id FROM customers WHERE phone = num;

            SELECT VideoVer INTO ver FROM video WHERE videoId = vidID;
               
            INSERT INTO hire VALUES ( id, vidID, ver, current_date(), NULL);

        END;
    """

    cur.execute("DROP PROCEDURE IF EXISTS sp_HireOutMovie;")

    cur.execute(create_sp_query)
    conn.commit()

    print("STORED PROCEDURE: sp_HireOutMovie CREATED...")
    print(" ")
    print(" ")
#=========================================================================


    print("******************************************")
    print("Stored Procedures created successfully...")
    print("******************************************")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Incorrect user name or password!")

    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")

    else:
        print(err)

finally:
    cur.close()
    conn.close()


