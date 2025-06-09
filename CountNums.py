#Function to get seven values from a user
#Prompt user to enter VALUE_COUNT Numbers
#Input the number of values to prompt a user for
#Return a list with the values
def get_values_from_user_input(value_count):
    val_list = []
    for i in range(value_count):
        val_list.append(int(input("Enter a number: ")))
    return val_list

#Function to print key value pairs
#input -  a dictionary of key value pairs
def print_key_value_pairs(val_dict):
    #publish key value pairs
    for key, value in val_dict.items():
        print(str(key) + " appears " + str(value) + " times.")

#Function to generate a dictionary given a list of values
#Input: A list of values
#Output: A dictionary with key as number and value of how many times the number appears in the list
def generate_dictionary_from_list(list):
    #define an empty dictionary
    num_dict = {}
    #Loop through numbers in the list
    for num in list:
        #if a number is already a key in the dictionary
        if num in num_dict.keys():
            #increment the value
            num_dict[num] = num_dict[num] + 1
        #For a new value add, it to the list and assign a value of 1
        else:
            num_dict[num] = 1

    return num_dict

def main():
    #Define constant for how many values to prompt a user for
    VALUE_COUNT = 7

    #Get input values from user
    list_nums = get_values_from_user_input(VALUE_COUNT)

    #Create the dictionary of value and how many times the value appears in the list
    num_dict = generate_dictionary_from_list(list_nums)

    #Publish the dictionary contents
    print_key_value_pairs(num_dict)        

if(__name__ == "__main__"):
    main()
