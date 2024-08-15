#============================================================
#This script is for testing 
#pulling value from database var to python var.
#============================================================


import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(user = "root",
        passwd = "123456",
        host = "localhost",
        database = "world")

    cur = conn.cursor()
    
    call1 = "call sp_Check_ClientExists('"
    city_Name = 'Kabo'
    call2 = "')"
    
    # call sp_Check_ClientExists("+ city_Name +")
    call_CheckClientExist = call1 + city_Name + call2

    cur.execute(call_CheckClientExist)

    result = cur.fetchone()[0]

    print(f"The found value: {result}")

    cur.close()
    conn.close()

       
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Incorrect user name or password!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists")
    else:
        print(err)
