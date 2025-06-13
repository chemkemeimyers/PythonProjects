import random
import matplotlib.pyplot as plt
import time

STUDENT_NUM = 10
ADDITIONAL_INPUT_COUNT = 3
print("Hi, You are a teacher looking for input on what to teach in computer science. Please add " + str(ADDITIONAL_INPUT_COUNT) + " more topics for students to select:")


python_poll = {"Question": "What python concept would you like to learn?",
               "options":{"Graphics":0, 
                          "Functions":0, 
                          }}

def addTopic(dictionary):
    message = ""
    if (dictionary == python_poll):
        message = "Enter a computer science topic for students to select from: "
    else:
        message = "Enter a snack suggestion for class: "
    dictionary["options"].update({input(message):0})
    
print("\nTo start we have the below topics included: ")
for topic in python_poll.values():
    print(topic)

print("\nAdd " + str(ADDITIONAL_INPUT_COUNT) + " more topics for selection: ")
for i in range (ADDITIONAL_INPUT_COUNT):
    addTopic(python_poll)

count_students = input("\nEnter the number of students in the class: ")

STUDENT_NUM = int(count_students)

print("We simulate a class of " + str(STUDENT_NUM) + " voting for their favorite topic using the random library to simulate voting: ")

print("\n" + python_poll["Question"])
for i, option in enumerate(python_poll["options"], start=1):
    print(f"{i}. {option}")

print("\nSimulating voting....")

time.sleep(3)

def takePollNGraph(poll_detail):

    options = list(poll_detail["options"].keys())
    for i in range (STUDENT_NUM):
        choice = random.choice(options)
        poll_detail["options"][choice] +=1

    print(f"\nResults for poll: {poll_detail['Question']}")
    for option, votes in poll_detail["options"].items():
        bar = "█" * votes
        print(f"{bar} {option:<10}:{votes} votes")

    options = list(poll_detail["options"].keys())
    votes = list(poll_detail["options"].values())
    colors = plt.cm.Pastel1.colors

    #Create a pie chart
    plt.figure(figsize=(7,7))
    plt.pie(votes, labels = options, autopct="%1.1f%%", startangle=140, colors=colors)
    plt.title(poll_detail['Question'])
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def rankPoll(poll_detail, comment):
    sorted_items = sorted(poll_detail['options'].items(), key=lambda x:x[1], reverse=True)
    print(f"🏆 Top 3 {comment}:")
    for i, (item, votes) in enumerate(sorted_items[:3], 1):
        print(f"{i}. {item}: {votes} votes")

takePollNGraph(python_poll)

rankPoll(python_poll, "Topics")

print("Hi, You would like to find out what snacks the class would be interested in for special occasions. Please add " + str(ADDITIONAL_INPUT_COUNT) + " more snack ideas for students to select:")

food_poll = {"Question": "What would you like to eat?",
             "options":{"Pizza":0,
                        "Cookies":0,
                        }}
    
print("\nTo start we have the below topics included: ")
for idea in food_poll.values():
    print(idea)

print("\nAdd " + str(ADDITIONAL_INPUT_COUNT) + " more snack suggestions for selection: ")
for i in range (ADDITIONAL_INPUT_COUNT):
    addTopic(food_poll)

print("We simulate a class of " + str(STUDENT_NUM) + " voting for their favorite snack using the random library to simulate voting: ")

print("\n" + food_poll["Question"])
for i, option in enumerate(food_poll["options"], start=1):
    print(f"{i}. {option}")

print("\nSimulating voting....")

time.sleep(3)

takePollNGraph(food_poll)

rankPoll(food_poll, "snacks")

