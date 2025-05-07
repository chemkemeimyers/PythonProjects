import random
"""
Simple program to teach addition. 
It provides a user with an addition problem, accepts an answer from the user and checks the users answer and provides feedback
"""
def main():
    print("Khansole Academy")
    #Generate two random integer between 10 and 99
    random_num1 = random.randint(10, 99)
    random_num2 = random.randint(10, 99)

    #get and print user answer
    print(f"What is {random_num1} + {random_num2}?")
    user_answer = input("Your answer: ")

    #Check is the user answer is correct
    if(int(user_answer) == (random_num1 + random_num2)):
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {random_num1 + random_num2}")

    
    
    
if __name__ == '__main__':
    main()