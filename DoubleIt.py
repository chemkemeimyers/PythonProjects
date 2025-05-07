def main():
    """
    Program to prompt a user for a number and then the program doubles it until it reaches a value of 100 or greater
    """
    #prompt user for a number
    curr_value = int(input("Enter a number: "))

    while(curr_value < 100):
        #Double the value
        curr_value = curr_value * 2
        #Print the doubled value
        print(curr_value)
    

if __name__ == '__main__':
    main()