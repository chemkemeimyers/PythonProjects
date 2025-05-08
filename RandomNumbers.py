import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

"""
A function to generate a random number between min value and max value
"""
def generate_random_number():
    return random.randint(MIN_VALUE, MAX_VALUE)

def main():
    """
    A program to print a series of 10 random numbers. The numbers are in the range 1 to 100
    """
    for i in range(N_NUMBERS):
        print(str(generate_random_number()))

if __name__ == '__main__':
    main()