'''
Function to count the number of vowels in a word
Input: A string
Output: An integer count of the number of vowels in the word
'''
def count_vowels(word):
    count = 0
    vowels = ['a','e','i','o','u']
    for character in word:
        if(character.lower() in vowels):
            count+=1

    return count

#word variable
word = "Hello"
#print statement to check result
print(word + " has " + str(count_vowels(word)) + " vowels.")