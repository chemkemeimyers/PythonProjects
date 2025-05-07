import random
"""
program to let user specify the number of sides on a dice and print a random number between 1 and the number of sides of the die
"""
def main():
    dice_side_count = input("How many sides does your dice have? ")

    dice_side_count = int(dice_side_count)

    roll = random.randint(1, dice_side_count)

    print(f"Your roll is {roll}")

if __name__ == '__main__':
    main()