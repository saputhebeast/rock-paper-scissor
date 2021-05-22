# importing required modules
import mysql
import mysql.connector

# defining a function to check if there are any values existing in the database
def isThereValues():

    # open database connection
    db = mysql.connector.connect( host="localhost", user="root", password="root", database="rps" )
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # check if there are any existing  values in the database
    sql = "select * from points ORDER BY Rounds DESC LIMIT 1;"

    # execute SQL query using execute() method
    cursor.execute( sql )
    
    # create values as a global variable
    global values

    # get database data to values variable
    values = [ list( item ) for item in cursor ]

    # return values
    return values

# defining a function to clear previous game data
def clear( values ):

    # a loop to ask if the user wants to clear the game data or not
    loop = True

    # looping
    while loop:

        # Notifying the user that there are previous game data in the database
        print( "\n" )
        print( "".center( 80, '-' ) )
        print( " We found previous game data in the database ".center( 80, '-' ) )
        print( "".center( 80, '-' ) )
        
        # Asking user whether to clear previous data
        print( "" )
        clearData = input( "Do you want to clear previous data? (y/n) : " ).lower()
        # Checking if there are any values in the points table inside the database
        if len( values ) > 0:
            
            # the bellow code segment only works if the user wants to clear game data
            if clearData == 'y':
                
                # open database connection
                db = mysql.connector.connect( host = 'localhost', database = 'rps', user = 'root',password = 'root' )
                
                # prepare a cursor object using cursor() method
                cursor = db.cursor()
                
                # execute SQL query using execute() method
                cursor.execute( "DELETE FROM points" )
                
                # commit changes
                db.commit()
                
                # notifying the user that the database was cleared successfully
                print( "\nDatabase cleared successfully!" )
                
                # end while loop
                loop = False
                
            # the below code segment only works if the user doesn't want to clear game data
            elif clearData == 'n':
                
                # end while loop without clearing database
                loop = False

# defining a function to call isThereValues and clear functions
def clearData():

    # call clear function when isThereValues function becomes True
    if isThereValues():
        clear( values )