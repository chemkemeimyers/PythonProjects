'''
Program to create a memory game
'''
import random

NUM_PAIRS = 3

def main():
    listNums = createNumPairsList()
    #print the original list
    print("The original list: ")
    print(listNums)
    #Shuffle the numbers
    random.shuffle(listNums)
    print("The shuffled list: ")
    print(listNums)

    guessList = initializeGuessList()
    print(guessList)

    print(get_valid_index(guessList))

    
    #print initial guessList
    print(guessList)

    
    #Print the displayedlist
    #displayVisibleList(listNums,guessList)

'''
A function to create an initial state of the guess list
In this specific case, the values of the numbers are 0, 1, 2 repeated twice
When we initialize a guess list with all 3's, we ensure there is no match
'''
def initializeGuessList():
    guessList = []
    for i in range(NUM_PAIRS * 2):
        guessList.append('*') ## A value that would not be in the initial items to be guessed

    return guessList  


'''
Function to get a valid index guess from the user
Input: The diplayed list
Output: Returned index
'''

def get_valid_index(display_list):
    valid_index = False
    valid_guess_index = 99


    while(not valid_index):
        guess_index_is_a_digit = False
        guess_index_is_in_correct_range = False
        guess_index_is_a_new_unique_index = False
        
        guess_index = input("Enter an index: ")

        if not guess_index.isdigit():
            print("Not a number. Try again.")
        else:
            guess_index = int(guess_index)
            guess_index_is_a_digit = True

            if(guess_index < 0 or guess_index >= NUM_PAIRS * 2):
                print("Invalid index. Try again.")
            else:
                guess_index_is_in_correct_range = True
        
                if(display_list[guess_index] != '*'):
                    print("This number has already been matched. Try again.")
                else:
                    guess_index_is_a_new_unique_index = True
        
        if(guess_index_is_a_digit and 
           guess_index_is_in_correct_range and
           guess_index_is_a_new_unique_index):
            valid_guess_index = guess_index
            valid_index = True
        
    return valid_guess_index



'''
Function to request 2 valid guesses from the player.
The function returns a list of 2 valid integer values
'''
def get_two_valid_indexes(guessList):
    guessIndexes = []
    while(len(guessIndexes) < 2):
        guess = int(input("Enter an index: "))

        if(guess >= 0 and guess < NUM_PAIRS * 2):
            if(guessList[guess] != '*'):
                if(len(guessIndexes) > 0 and guessIndexes[0] != guess):
                    guessIndexes.append(guess)
                else:
                    print("Invalid index. Try again.")
            else:
                print("Invalid index. Try again.")
        else:
            print("Invalid index. Try again.")
    
    return guessIndexes



'''
Function to create a list with pairs of repeating numbers
'''
def createNumPairsList():
    num_list = []
    for i in range(NUM_PAIRS):
        for j in range (2):
            num_list.append(i)
    return num_list

'''
Function to print the displayedlist
'''
def displayVisibleList(listNums, guessList):
    displayList = []
    for i in range(len(listNums)):
        displayList.append('*')
    for i in range(len(listNums)):
        if (listNums[i] == guessList[i]):
            displayList[i] = listNums[i]
    print(displayList)

def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()