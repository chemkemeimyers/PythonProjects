from ai import call_gpt

def main():
    """
    program to get user name and topic and to use call_gpt to create a brief Haiku
    """

    name = input("Enter your name: ")

    topic = input("Enter a topic: ")

    print("Creating your haiku ....")

    message = f"Create haiku for {name} on {topic}"

    print(call_gpt(message))


if __name__ == "__main__":
    main()