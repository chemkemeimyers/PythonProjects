'''
A game to accept increasing values of numbers. 
When the user enters a number which is smaller 
than their previously entered value, the program is over. 
Tell the user how long their sequence was.
'''

#Function that returns True if the second value is larger or equal to the first value
def increasing(num1, num2):
    if(num2 >= num1):
        return True
    else:
        return False

def main():
    sequence_length = 0

    print("Enter a sequence of non-decreasing numbers.")
    val1 = input("Enter num: ")
    sequence_length += 1 #count the first value
    val2 = input("Enter num: ")

    while(increasing(float(val1),float(val2))):
        val1 = val2
        sequence_length+=1
        val2 = input("Enter num: ")
    
    print("Thanks for playing! ")
    print("Sequence length: " + str(sequence_length))

if __name__ == "__main__":
    main()