import random
import matplotlib.pyplot as plt

print("Hi, this is a poll to explore the interests of 10 random subjects:")

python_poll = {"Question": "What python concept would you like to learn?",
               "options":{"Graphics":0, 
                          "Functions":0, 
                          "AI and Random Libraries":0,
                          "While, if statements, and loops":0,
                          "Lists and dictionaries":0}}

food_poll = {"Question": "What would you like to eat?",
             "Options":{"Pizza":0,
                        "Curry":0,
                        "Burritos":0,
                        "Salad":0,
                        "Ugali":0,
                        "Gyro":0,
                        "Sandwich":0}}

activity_poll = {"Question": "What would you like to do today?",
                 "Options":{"Code in place":0,
                            "Hike":0,
                            "Relax":0,
                            "Visit firends":0,
                            "Go to the park with family":0}}

voter_names = ["Alice", "Bob", "Susan", "Claire", "Mat", "Alex",
               "Kristy", "Tom", "Ben", "Maria"]

print("\n" + python_poll["Question"])
for i, option in enumerate(python_poll["options"], start=1):
    print(f"{i}. {option}")

options = list(python_poll["options"].keys())
for i in range (len(voter_names)):
    choice = random.choice(options)
    python_poll["options"][choice] +=1
    print("Voter " + voter_names[i] + " selected option: " + choice)

print(f"\nResults for poll: {python_poll['Question']}")
for option, votes in python_poll["options"].items():
    bar = "█" * votes
    print(f"{bar} {option:<10}:{votes} votes")

options = list(python_poll["options"].keys())
votes = list(python_poll["options"].values())
colors = plt.cm.Pastel1.colors

#Create a pie chart
plt.figure(figsize=(7,7))
plt.pie(votes, labels = options, autopct="%1.1f%%", startangle=140, colors=colors)
plt.title(python_poll['Question'])
plt.axis('equal')
plt.tight_layout()
plt.show()

""" plt.bar(options, votes, color='skyblue')
plt.title(python_poll['Question'])
plt.xlabel("Options")
plt.ylabel("Votes")
plt.tight_layout()
plt.show() """