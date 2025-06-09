# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

#method to return text odd for 'odd' numbers and 'even' for even numbers
def check_odd_or_even(num):
    if(num % 2 > 0):
        return "odd"
    else:
        return "even"

def main():
    #Print if value is odd or reven from 0 to MAX_NUMBER
    for i in range(MAX_NUMBER):
        i = i + 1 #Since python starts counting at 0 and we need to check odd and even behaviour for values 1 to MAX_NUMBER. Increment i + 1
        print(str(i) + " is " + check_odd_or_even(i))

if __name__ == "__main__":
    main()