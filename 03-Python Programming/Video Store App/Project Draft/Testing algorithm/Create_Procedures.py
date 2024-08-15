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
        database="world")

    cur = conn.cursor()


    create_sp_query = """
        CREATE PROCEDURE sp_Check_ClientExists(IN str VARCHAR(40))
        BEGIN
            DECLARE i INT;
            DECLARE bFound BOOL;

            SELECT COUNT(District) INTO i FROM city WHERE District = str;

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

    print("******************************************")
    print("Stored Procedure created successfully...")
    print("******************************************")

    conn.commit()

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


