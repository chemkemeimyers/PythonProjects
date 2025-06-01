def main():
    num_list = [3, 4, 6, 7, 3, 9, 4, 3, 7]
    num_dict = {}

    #Loop through numbers in the list
    for num in num_list:
        #if a number is already a key in the dictionary
        if num in num_dict.keys():
            #increment the value
            num_dict[num] = num_dict[num] + 1
        #For a new value add, it to the list and assign a value of 1
        else:
            num_dict[num] = 1
    #publish key value pairs
    for key, value in num_dict.items():
        print(str(key) + " -> " + str(value))

if(__name__ == "__main__"):
    main()
