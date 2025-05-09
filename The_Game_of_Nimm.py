def main():
    """
    Program to create the ancient game of Nimm
    """
    #Variable for initial number of stones
    START_NUM_STONES = 20

    num_stones_left = START_NUM_STONES
    player = 1

    """
    Function to print the number of stones left, the function takes as input the number of stones left
    """
    def print_num_stones(num_stones_left):
        print(f"There are {num_stones_left} stones left.")
        
    
    while(num_stones_left > 0):
        #Initialize variable to check for valid input at True
        input_is_invalid = True
        #Print initial number of stones
        print_num_stones(num_stones_left)

        #Remove stones based on user input
        msg = f"Player {player} would you like to remove 1 or 2 stones? "
        user_input = int(input(msg))

        #Check is user has provided a valid input
        if(user_input !=1 and user_input != 2):
            input_is_invalid = True
        else:
            input_is_invalid = False
        #Continue to prompt user for valid input
        while(input_is_invalid):
            user_input = int(input("Please enter 1 or 2: "))

            #When user provides a valid input reset input_is_invalid
            if(user_input == 1 or user_input == 2):
                input_is_invalid = False

        num_stones_left = num_stones_left - user_input
        print()

        if(player == 1):
            player = 2
        else:
            player = 1
    
    if(player == 1):
        print("Player 1 wins!") #When the game ends the players are switched. If player = 1, that means the last player to pull stones was player 2, so player 1 wins!
    else:
        print("Player 2 wins!")

if __name__ == '__main__':
    main()