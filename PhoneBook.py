'''
Program to create a phone book and enable look-up for entries in the phone book
'''

#Function to get name and phone number from users and return a dictionary
#The method runs until the user provides an empty input value
#Once there is no user input provided, this method returns a dictionary
def get_user_input_for_phone_dict():
    phonebook_dict = {}

    name_entry = input("Name: ")

    while(name_entry != ""):
        phonebook_dict[name_entry] = input("Number: ")
        name_entry = input("Name: ")

    return phonebook_dict

#Function to check for a users details in the phonebook dictionary
#Prompt user for the name to look up
#If the user is in the phone dictionary, provide the user's phone number
#If the user is NOT in the phone dictionary, state that the user is NOT in the phone book
#Stop checking when the user provides empty input
def check_dictionary(phone_dict):
    look_up_name = input("Enter name to look up: ")

    while(look_up_name != ""):
        #Check if the name is in the dictionary keys
        if look_up_name in phone_dict.keys():
            print(phone_dict[look_up_name])
        else:
            print(look_up_name + " is not in the phonebook")

        look_up_name = input("Enter name to look up: ")

#Function to publish key value pairs in a phone book dictionary
def publish_phonebook(phonebook_dict):
    for key, value in phonebook_dict.items():
        print(key + " -> " + value)

def main():
    #prompt users to add names and phone numbers to the phonebook
    #store the returned dictionary
    phonebook_dict = get_user_input_for_phone_dict()

    #publish the phonebook
    publish_phonebook(phonebook_dict)

    #Check for users in the phone book and publish the corresponding phonenumbers
    check_dictionary(phonebook_dict)

if (__name__ == "__main__"):
    main()