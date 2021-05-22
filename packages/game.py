# importing required modules
# importing required modules
# importing required modules
import packages.prettyTable
import packages.sendData
import random

# defining main logic
def mainLogic():
    
    # assigning a variable called play as true for looping 
    play = True

    # assigning variables to count scores (game data)
    totalGamePlays = 0
    draws = 0
    userWins = 0
    computerWins = 0
    
    # loop for user to play the game as long as he/she wants
    while play:
        
        # gets user's choice and convert userChoice to lowercase
        userChoice = input( "\nEnter your choice (r/p/s): " ).lower()
        
        # check whether the user's choice matches with avaliable choices 
        if userChoice == 'r' or userChoice == 'p' or userChoice == 's':
            
            # Pass if true
            pass
        
        # the bellow code segment runs when the user's input does not match with the avaliable choices
        else:

            # get the correct user input using a while loop
            while True:
                
                # ask again from the user to enter a valid input
                userChoice = input( "\nPlease enter a valid letter : " ).lower()
                
                # check whether the user's choice matches with avaliable choices
                if userChoice == 'r' or userChoice == 'p' or userChoice == 's':
                    
                    # break the loop when user input the correct input
                    break
                
        # counting total game plays     
        totalGamePlays += 1
        
        # check user choice
        if userChoice ==  'r':
            userChoice = 'rock'
        elif userChoice == 'p':
            userChoice = 'paper'
        else:
            userChoice = 'scissor'

        # add rock, paper, scissor, values to item list
        items = [ "rock", "paper", "scissor" ]

        # get random value from item list
        computerChoice = random.choice( items )

        # check draw or not
        if computerChoice == userChoice:
            
            # add 1 point to draw when computerChoice is equal to userChoice
            draws += 1
            
            # print draw
            print( "\n Game Drawn!" )

        # check who wins
        if userChoice == 'rock' and computerChoice == 'scissor':
            
            # add 1 point to user when user wins over computer
            userWins += 1
            
            # print user win
            print( "\n You Won!" )
            
        elif userChoice == 'scissor' and computerChoice == 'paper':
        
            # add 1 point to user when user wins over computer
            userWins += 1
            
            # print user win
            print( "\n You Won!" )
        
        elif userChoice == 'paper' and computerChoice == 'rock':
            
            # add 1 point to user when user wins over computer
            userWins += 1
            
            # print user win
            print( "\n You Won!" )
            
        elif computerChoice == 'rock' and userChoice == 'scissor':
            
            # add 1 point to computer when computer wins over user
            computerWins += 1
            
            # print computer win
            print( "\n Computer Won!" )
        
        elif computerChoice == 'scissor' and userChoice == 'paper':
            
            # # add 1 point to computer when computer wins over user
            computerWins += 1
            
            # print computer win
            print( "\n Computer Won!" )
        
        elif computerChoice == 'paper' and userChoice == 'rock':
            
            # add 1 point to computer when computer wins over user
            computerWins += 1
            
            # print computer win
            print( "\n Computer Won!" )

        #print black line for better understanding
        print()
        
        # asking if the user wants to play again and convert user input to lowercase
        playOrNot = input( "\nDo you want to play again? (y/n) : " ).lower()
        
        # check if user wants to stop playing
        if playOrNot == 'n':
            
            # send data to database
            packages.sendData.storeData( totalGamePlays, computerWins, userWins, draws )
            
            # print the pretty table
            packages.prettyTable.table()
            
            # assign false to play to exit the loop
            play = False

        # check is user wants to play again
        elif playOrNot == 'y':
            
            # assign True to 'play' to continue the loop
            play = True
        
        # if user enters an invalid letter/input
        else:
            
            # assigning 'again' as true for looping
            again = True
            
            # loop when 'again' becomes true
            while again:
                
                # ask again to enter valid input
                playOrNot = input( "\nPlease enter a valid letter : " ).lower()
                
                # if the user does not want to play again
                if playOrNot == 'n':
                    
                    # send data to database
                    packages.sendData.storeData( totalGamePlays, computerWins, userWins, draws )
                    
                    # print prettytable
                    packages.prettyTable.table()
                    
                    # quit the game
                    again = False
                    play = False
                    
                # check is user wants to play again 
                elif playOrNot == 'y':
                    
                    # continue playing the game
                    play = True
                    
                    # exit the nested loop
                    again = False