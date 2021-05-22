# importing required modules
import mysql
import mysql.connector
from mysql.connector import Error

# defining function to check connectivity with the MySQL server
def connectivity():
    # open database connection
    db = mysql.connector.connect( host = 'localhost',user = 'root',password = 'root' )

    # create an empty list to append databases
    databases = []

    # create an empty list to append tables
    tables = []

    # check if MySQL servers connected successfully
    try:
        if db:
            print( "\nMySQL server is connected successfully..." )

    # print error message, if MySQL servers doesn't connected successfully
    except Error as e:
        print( "Error" )
        print( e )
        print("\n")
        print( "Cannot connect with MySQL server!" )


    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # execute SQL query using execute() method
    cursor.execute( "SHOW DATABASES" )

    # fetch results using fetchall() method
    data = cursor.fetchall()

    # append databases to database list
    for item in data:
        databases.append( *item )

    # disconnect from server
    db.close()


    # check if rps database is not in the databases list
    if 'rps' not in databases:

        # print a message notifying the user when the rps database is not found
        print( "No database found!" )

        # open database connection
        db = mysql.connector.connect( host = 'localhost',user = 'root',password = 'root' )

        # prepare a createdcursor object using cursor() method
        createdcursor = db.cursor()
        
        # execute SQL query using execute() method
        createdcursor.execute( "CREATE DATABASE rps" )
        
        # print a message notifying the user when the rps database is created successfully
        print( "The database has been created successfully..." )
        
        # works when createdcursor object becomes true
        if createdcursor:
            
            # open database connection
            db = mysql.connector.connect( host = 'localhost',user = 'root',password = 'root', database = 'rps' )
            
            # prepare a usecursor object using cursor() method
            usecursor = db.cursor()
            
            # execute SQL query using execute() method
            usecursor.execute( "USE rps" )
            
            # print a message notifying the user when the rps database is used successfully
            print( "Using database : rps" )
            
            # works when usecursor object becomes true
            if usecursor:

                # open database connection
                db = mysql.connector.connect( host = 'localhost',user = 'root',password = 'root', database='rps' )
            
                # prepare a tablecursor object using cursor() method
                tablecursor = db.cursor()
            
                # execute SQL query using execute() method
                tablecursor.execute( "CREATE TABLE points ( Rounds VARCHAR( 999 ), Computer_Wins VARCHAR( 999 ), User_Wins VARCHAR( 999 ), Draws VARCHAR( 999 ) );" )
            
                # print a message notifying the user when the points table is created successfully
                print( "Points table has been created successfully..." )

    # works when rps database in databases list
    else:

        # open database connection
        db = mysql.connector.connect( host = 'localhost',user = 'root',password = 'root', database = 'rps' )
        
        # prepare a usecursor object using cursor() method
        usecursor = db.cursor()
        
        # execute SQL query using execute() method
        usecursor.execute( "USE rps" )
        
        # print a message notifying the user when the rps database is used successfully
        print( "rps database has been used successfully..." )
        
        # open database connection
        db = mysql.connector.connect( host = 'localhost',user = 'root',password = 'root', database = 'rps' )
        
        # prepare a tablecursor object using cursor() method
        tablecursor = db.cursor()
        
        # execute SQL query using execute() method
        tablecursor.execute( "show tables" )
        
        # append tables to tables list
        for item in tablecursor:
            tables.append(*item)
        
        # check if points table is not in the tables list
        if 'points' not in tables:
            
            # open database connection
            db = mysql.connector.connect( host = 'localhost',user = 'root',password = 'root', database='rps' )
            
            # prepare a tablecursor object using cursor() method
            tablecursor = db.cursor()

            # execute SQL query using execute() method
            tablecursor.execute( "CREATE TABLE points (Rounds VARCHAR(999), Computer_Wins VARCHAR(999), User_Wins VARCHAR(999), Draws VARCHAR(999));" )

            # print a message notifying the user when the points table is created successfully
            print( "Points table has been created successfully..." )