
'''
Program to compute average from list of numbers in a file
'''
def main():
    number_list = load_numbers_from_file("numbers.txt")
    print("Average: " + str(computeAverage(number_list)))

#Function to compute average when given a list of numbers
#Input: List of numbers
#Output: The average value
def computeAverage(numbers):
    return sum(numbers)/len(numbers)


#Function to load a numbers list from a text file
def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    
    return numbers


if __name__ == '__main__':
    main()
