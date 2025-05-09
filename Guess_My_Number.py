"""
Program that generates a random integer value and guides the user to guess it
"""
import random

def main():
    #get the random number
    START = 1
    END = 99
    random_num = random.randint(START, END)
    #get user guess
    print(f"I am thinking of a number between {START} and {END}...")
    guess = get_user_guess()
    guess_Match = False
    while(not guess_Match):
        guess_Match = check_guess(guess, random_num)
        #get new user input
        if(not guess_Match):
            guess = get_user_guess()

"""
Function to get the user's guess and return it as an int
"""
def get_user_guess():
    guess = int(input("Enter a guess: "))
    return guess

"""
Function to compare the guess and the random number
The function prints comment indicating:
 - if the guess and random number are matched
 - if the the guess is higher than the random number
 - if the guess is lower than the random number
 Function returns true when the guess matches the random number
 Function returns false when the guess does not match the random number
 """
def check_guess(guess, random_num):
    if(guess == random_num):
        print(f"Congrats! The number was: {random_num}")
        return True
    elif(guess < random_num):
        print("Your guess is too low")
        return False
    else:
        print("Your guess is too high")
        return False

if __name__ == '__main__':
    main()