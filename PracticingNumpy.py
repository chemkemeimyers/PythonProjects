import numpy as np
#Define a list of different cars
arr_str = ["Mercedes", "BMW", "Audi","Ferrari","Tesla"]

#Define the number of cylinders in a car
arr_num = [5, 4, 6, 7, 3]

#Printing the elements in the string
for name in arr_str:
    print(name)

#Converting the list arr_str to a Numpy array
np_arr_str = np.array(arr_str)

np_arr_num = np.array(arr_num)

#Check the output
print("Numpy Array (arr_str)", np_arr_str)
print("Numpy Array (arr_num): ", np_arr_num)

#Check the type
print("Type of arr_str: ", type(arr_str))
print("Type of arr_num: ", type(arr_num))

print("Type of np_arr_str: ", type(np_arr_str))
print("Type of np_arr_num: ", type(np_arr_num))

matrix = np.array([[1, 2, 1], [4, 5, 6], [1, 8, 9]])
print(matrix)

print("Data type of matrix: ", type(matrix))

print(list(range(0,9)))