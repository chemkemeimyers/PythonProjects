'''
Program to create a memory game
'''
import random

NUM_PAIRS = 3

def main():
    listNums = createNumPairsList()
    print("The original list: ")
    print(listNums)
    random.shuffle(listNums)
    print("The shuffled list: ")
    print(listNums)

'''
Function to create a list with pairs of repeating numbers
'''
def createNumPairsList():
    num_list = []
    for i in range(NUM_PAIRS):
        for j in range (2):
            num_list.append(i)
    return num_list

def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()