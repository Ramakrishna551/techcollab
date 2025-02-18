#1. Create a function that takes dimensions as tuples e.g. (3, 3) and a numeric
# value and returns a NumPy array of the given dimension filled with the
# given value e.g.: solve((3, 3), 5) will return
# [
# [5, 5, 5],
# [5, 5, 5],
# [5, 5, 5]
# ]
#ans
import numpy as np
def fun(dimensions,value):
    return np.full(dimensions,value)

print(fun((3,3),5))
#2.Create a method that takes n NumPy arrays of the same dimensions,
# sums them and returns the answer

def sum_arrays(*arrays):
    return  np.sum(arrays, axis=0)
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
arr3 = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
print(sum_arrays(arr1, arr2, arr3))

#3.Given a 2 D Array of N X M Dimension, write a function that accepts this
# array as well as two numbers N and M. The method should return the
# top-left N X M sub matrix, e.g:
# [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# ]

def get_submatrix(array, N, M): #here :N indicates the 2nd row and M: indicates excludes the 2nd column from the array
    return array[:N, :M]
    
print(get_submatrix(arr1, 2, 2))

#sub_matrix(matrix, 1, 1) -> should return : (Keep in mind these arrays are
# zero indexed)
def get_submatrix(array, row, col):
    return array[row:,col:]
# Extracting a submatrix
print(get_submatrix(arr1, 1, 1))

#5.Given a 1 D NumPy Array. Write a function that accepts this array as
# parameters. The method should return a dictionary with 'mean' and
# 'std_dev' as key and array's mean and array's standard deviation as
# values:
# [1, 1, 1]
# solution(arr) -> should return :
# {'mean': 1.0, 'std_dev': 0.0}

def solution(arr):
    mean = np.mean(arr)  # Calculate the mean of the array
    std_dev = np.std(arr)  # Calculate the standard deviation of the array
    return {'mean': mean, 'std_dev': std_dev}

# Example usage:
arr = [1, 1, 1]
result = solution(arr)
print(result)