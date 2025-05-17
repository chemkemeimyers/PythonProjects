
def main():
    for i in range(10, 20):
        if(IsOdd(i)):
            print(i, "odd")
        else:
            print(i, "even")

def IsOdd(i):
    return i % 2 > 0

if __name__ == '__main__':
    main()