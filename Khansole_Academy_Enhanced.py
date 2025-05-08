import random
PROBLEM__TO_SOLVE_IN_ROW = 3
"""
Simple program to teach addition. 
It provides a user with an addition problem, accepts an answer from the user and checks the users answer and provides feedback
"""

"""
Function to sum two numbers
"""
def generate_addition_problem(num1, num2):
     print(f"What is {num1} + {num2}?")

"""
Function to check if the answer (sum of two numbers) provided by the user is correct
"""
def check_answer(answer, num1, num2):
    #Check is the user answer is correct
    if(int(answer) == (num1 + num2)):
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {num1 + num2}")

"""
Function to return 1 of the user provides the correct answer or 0 of the user does not provide the correct answer
"""
def increment_correct_responses(answer, num1, num2):
    if(num1 + num2 == answer):
        return 1
    else:
        return 0


def main():
    print("Khansole Academy")

    correct_responses = 0

    """
    Continue to give summation problems until a user provides 3 consecutive correct responses
    """
    while(correct_responses < 3):

        #Generate two random integer between 10 and 99
        random_num1 = random.randint(10, 99)
        random_num2 = random.randint(10, 99)

        #get and print user answer
        generate_addition_problem(random_num1, random_num2)
        user_answer = input("Your answer: ")

        #Check if the user provided the correct answer
        check_answer(int(user_answer), random_num1, random_num2)

        if(increment_correct_responses(int(user_answer), random_num1, random_num2) == 1):
            correct_responses += 1
            print(f"You've gotten {correct_responses} correct in a row. ")
        else:
            correct_responses = 0

    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()