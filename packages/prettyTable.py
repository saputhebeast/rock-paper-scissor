# importing required modules
import html
from prettytable import PrettyTable
import mysql
import mysql.connector

# define a function to create the prettytable
def table():
    # assigning prettytable to a variable
    x = PrettyTable( [ "Total Game Plays", "Total Computer Wins", "Total User Wins", "Total Draws" ] )
    
    # open database connection
    db = mysql.connector.connect( host = 'localhost', user = 'root', password = 'root', database = 'rps' )

    # prepare a cursor object using cursor method
    cursor = db.cursor()

    # execute SQL query using execute() method
    cursor.execute( "SELECT * FROM points" )

    # fetch results using fetchall() method
    data = cursor.fetchall()
    
    # add data to prettytable
    for item in data:
        x.add_row( item )
    table = x

    # set table border in html file 
    html = x.get_html_string()
    html = html.replace( "<table>", "<table border = 1>" )

    # open html file as stats.html to write table data
    file = open( "stats.html","w" )

    # write data
    file.write( html )

    # close file
    file.close()

    # print prettytable 
    print( table )