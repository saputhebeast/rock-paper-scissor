# importing required modules
import packages.connect
import packages.rules
import packages.game
import packages.clear

# defining main function to call the other modules
def main():

    # check connectivity with the SQL server
    packages.connect.connectivity()

    # clearing the existing values in the database or not
    packages.clear.clearData()

    # display the game rules
    packages.rules.gameRules()

    # call main logic of the game
    packages.game.mainLogic()

# call main function
main()
