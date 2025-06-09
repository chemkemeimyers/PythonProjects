'''
Program to check if a user's height meets atronout requirements
'''

#Define constants for the height requirements
MAX_HEIGHT = 1.9
MIN_HEIGHT = 1.6

#Function that takes a height value and checks if the height meets astronout requirements
def check_astronout_height_requirement(height):
    if(height > MIN_HEIGHT and height < MAX_HEIGHT):
        print("Correct height to be an astronaut")

    elif(height <= MIN_HEIGHT):
        print("Below minimum astronaut height")
    
    elif(height >= MAX_HEIGHT):
        print("Above maximum astronaut height")
    
    else:
        print("Unexpected case observed!!!! Check input or program! ")
    
def main():
    #Get user height and cast it to float
    input_val = input("Enter your height in meters: ")

    try:
        input_height = float(input_val)
    except ValueError:
        print("That is not a valid number")

    #Call method to check astronaut height
    check_astronout_height_requirement(input_height)

if __name__ == "__main__":
    main()