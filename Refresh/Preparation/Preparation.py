#Lists: Dymanic and modifiable
fruits = ["apple", "pear", "orange"]
fruits.append("blueberry")

print(fruits)
print(dir(fruits))

#Tuple: Immutable protection
dimensions = (1920, 1000)

#Dictionary - key value pairs
user = {"name": "Alice",
        "age": 40,
        "City": "New York"}

print(user["name"])

#set - removes duplication
numbers = {1, 2, 2, 3, 4, 4, 5}

print(numbers)