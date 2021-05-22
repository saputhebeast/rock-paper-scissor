# importing required modules
import mysql
import mysql.connector

# defining function to store data in the database
def storeData( totalGamePlays, computerWins, userWins, draws ):
    
    # open database connection
    db = mysql.connector.connect( host = 'localhost', database = 'rps', user = 'root',password = 'root' )
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # SQL command to insert data into the points table
    insert = "INSERT INTO points (Rounds, Computer_Wins, User_Wins, Draws) VALUES (%s, %s, %s, %s)"

    # assign game data to the values variable
    values = ( totalGamePlays, computerWins, userWins, draws )

    # execute SQL query using execute() method
    cursor.execute( insert, values )

    # commint the changes
    db.commit()

    # disconnect from server
    db.close()