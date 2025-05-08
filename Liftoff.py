"""
Program: Liftoff
--------------------
Countdown from 10 to 1 and then print Liftoff!
"""
#Constant to store value to count down from
COUNTDOWN_START = 10
"""
function to decrement a value by 1
"""

def decrement_by_one(start):
    if(start > 0):
        return start-1

def main():
    start = COUNTDOWN_START
    while(start > 0):
        print(start)
        start = decrement_by_one(start)
        
    print("Liftoff!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()