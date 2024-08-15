#=========================================================================
#Name: Sopumelela
#Surname: Sandekela
#Student Number: CON-1475940-C5L6
#Module: Python Programming
#Script name: Application_Server_Side.py
#Discription: This module is a module for Inserting defualt values to the vide_store database.
#=========================================================================

import mysql.connector
from mysql.connector import errorcode
   
try:    
    conn = mysql.connector.connect(
    user = 'root',
    passwd = '123456',
    host = 'localhost',
    database = 'video_store')

#Insert values on Mysql with python
#INSERT values on customer table...
    cur = conn.cursor()

    cur.execute("""
            INSERT INTO customers (fname, sname, address ,phone ) 
            VALUES ('Thabo', 'Zulu', 'thabo.zulu@gmail.com', '0736533369'),
                   ('Kamva', 'Sgenu', 'Kamva.Sgenu@outlook.com', '0838358561'),
                   ('Sopumelela', 'Sandekela', 'MsoSands@gmail.com', '0605825283'),
                   ('Liyakha', 'Dangala', 'Likha.Dangala@gmail.com', '0739717723'),
                   ('Onzz', 'Jubeni', 'Onzz.Jubeni@gmail.com', '0627360131'),
                   ('Aphelele', 'Mbizana', 'Aphelele.Mbizana@gmail.com', '0820426643'),
                   ('Hlonela', 'Madubela', 'Clide.PapaBear@Yahoo.com', '0638561164');
        """)

    print("Defualt values have been added on table: customers")

    cur.close()
    conn.commit()
        

#INSERT values on video table...
    cur = conn.cursor()

    cur.execute("""
            INSERT INTO video (videoVer, vName, type ,dateAdded ) 
            VALUES ( 26, 'Spider-Man:Across the Spider-Verse', 'R', '2023-06-10'),
                   ( 3, 'Guardians of the Galaxy', 'B', '2014-08-05'),
                   ( 4, 'Citizen Kane', 'B', '2010-09-5'),
                   ( 11, 'Escape Plan', 'B', '2013-10-20'),
                   ( 7, 'Star Wars', 'B', '2010-08-12'),
                   ( 3, 'Aquaman &  the Lost Kingdom', 'R', '2023-12-28'),
                   ( 15, 'Titanic', 'B', '2010-12-20'),
                   ( 34, 'Mad Max: Fury Road', 'B', '2015-05-20'),
                   ( 24, 'Avengers: Endgame', 'B', '2019-04-30'),
                   ( 12, 'Spider-Man: No Way Home', 'R', '2021-12-21'),
                   ( 14, 'Avatar', 'B', '2010-12-17'),
                   ( 11, 'Apocalypto', 'B', '2010-12-08'),
                   ( 13, 'Avatar: The Way of Water', 'R', '2022-12-16'),
                   ( 6, 'The Matrix', 'B', '2010-03-31'),
                   ( 11, 'The Matrix Reloaded', 'B', '2010-05-15'),
                   ( 27, 'The Animatrix', 'B', '2010-06-03'),
                   ( 9, 'The Matrix Revolutions', 'B', '2010-11-05'),
                   ( 10, 'The Matrix Resurrections', 'R', '2021-12-30'),
                   ( 19, 'Back to the Future', 'B', '2010-07-03'),
                   ( 15, 'The Lord of the Rings', 'B', '2010-12-19'),
                   ( 24, 'The Equalizer 3', 'R', '2010-12-19');
        """)

    print("Defualt values have been added on table: video")

    cur.close()
    conn.commit()
     

#INSERT values on hire table...
    cur = conn.cursor()

    cur.execute("""
            INSERT INTO hire 
            VALUES ( 3, 17,  3, '2024-01-30', NULL),
                   ( 1, 5,  2, '2023-11-21', '2023-12-26'),                
                   ( 4, 12,  1, '2023-12-09', NULL),
                   ( 7, 2,  3, '2024-01-15', '2024-01-21'),
                   ( 5, 7,  5, '2023-12-11', NULL);
        """)

    print("Defualt values have been added on table: hire")

    cur.close()
    conn.commit()
    conn.close()

    print(" ")
    print("**************************************")
    print("All Default values have been added...")
    print("**************************************")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Incorrect user name or password!")
        
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")

    else:
        print(err)
