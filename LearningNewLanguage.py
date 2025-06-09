'''
Program to check for language translations, counting how many times 
a user gives the correct translation for a word in the dictionary
'''
#Fuction to get user translation for a given word
#input is the word to translate
#output is the translated word
def get_user_translation(word_to_translate):
    translation_prediction = input("What is the Spanish translation for " + word_to_translate + "?")
    return translation_prediction

#function to check if a user gives the correct translation for a word
#function takes the translation dictionary, the word translated and the user response
#if the translation prediction matches the true translation return 1
def check_correct(translations, key, translation_prediction):
    if(translations[key] == translation_prediction):
        print("That is correct!\n")
        return 1
    else:
        print("That is incorrect, the Spanish translation for " + key + " is "+ translations[key] + ".\n")
        return 0
    

def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    count_correct =  0

    for key in translations.keys():
        translation_prediction = get_user_translation(key)
        count_correct += check_correct(translations, key, translation_prediction)

    print("You got " +  str(count_correct) + "/" + str(len(translations)) + " words correct, come study again soon!")


if __name__ == '__main__':
    main()