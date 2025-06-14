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
    #print initial guessList
    print(guessList)

    
    #Print the displayedlist
    displayVisibleList(listNums,guessList)

def initializeGuessList():
    guessList = []
    for i in range(NUM_PAIRS * 2):
        guessList.append(NUM_PAIRS) ## A value that would not be in the initial items to be guessed

    return guessList  


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