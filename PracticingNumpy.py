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