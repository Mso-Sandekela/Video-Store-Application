#=========================================================================
#Name: Sopumelela
#Surname: Sandekela
#Student Number: CON-1475940-C5L6
#Module: Python Programming
#Script name: Creating_Database_And_Tables.py
#Discription: This script creates all the tables needed with 
#their correct data types and constraints. 
#=========================================================================
import mysql.connector
from mysql.connector import errorcode

try:
#=========================================================================
#Loging in using the video_store database/schema...
#=========================================================================
    conn = mysql.connector.connect(
        user = "root",
        passwd = "123456",
        host = "localhost",
        database = "video_store")
    #---------------------------------------------------------------------------------
    

    #The following block of code creates all the neccessary tables with their
    #keys and constraints.
    #---------------------------------------------------------------------------------

    #---------------------------------------------------------------------------------
    #                               Table: customers
    #---------------------------------------------------------------------------------
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE customers
                (
                    custId INT NOT NULL AUTO_INCREMENT,
                    fname VARCHAR(40)   NOT NULL,
                    sname VARCHAR(40)   NOT NULL,
                    address VARCHAR(40) NOT NULL,
                    phone VARCHAR(10)   NOT NULL,
                    PRIMARY KEY(custId),
                    UNIQUE(phone)
                );
            """)
    cur.close()
    print("Table customers created successfully...")
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
#                             Table: video
#---------------------------------------------------------------------------------
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE video
    (
    videoId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    videoVer    INT  NOT NULL,
    vName   VARCHAR(40) NOT NULL,
    type    VARCHAR(1)  NOT NULL,
    dateAdded   DATE    NOT NULL,
    CONSTRAINT CHK_DateAdded CHECK (dateAdded > current_date())
    );
    """)
    cur.close()
    print("Table video created successfully...")
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
#                               Table: hire
#---------------------------------------------------------------------------------
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE hire
        (
        custId INT NOT NULL,
        videoId INT NOT NULL,
        videoVer INT NOT NULL,
        dateHired DATE  NOT NULL,
        dateReturn DATE,
        PRIMARY KEY(custId, videoId),
        CONSTRAINT FK_CustId FOREIGN KEY(custId) REFERENCES customers(custId),
        CONSTRAINT FK_VideoId FOREIGN KEY(videoId) REFERENCES video(videoId),
        CONSTRAINT CHK_DateReturn CHECK (dateReturn < dateHired)
        );
        """)
    cur.close()
    print("Table hire created successfully...")
    conn.commit()
    conn.close()
#---------------------------------------------------------------------------------
    print(" ")
    print("*************************************")
    print("All tables Created successfully...")
    print("*************************************")
#---------------------------------------------------------------------------------

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Incorrect user name or password!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Datebase does not exist.")
    else:
        print(err)

#=========================================================================
#Creating Database/Schema completed successfully...
#=========================================================================
