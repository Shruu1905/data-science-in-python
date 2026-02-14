'''To create 2D , 3D array'''
import numpy as np 

arr_2D = np.array([[1,2,3] , [4,5,6]])

print(arr_2D)

arr_3D = np.array([[[1,2,3] , [4,5,6]]  ,  [[6,7,8] , [3,4,5]]])
print(arr_3D)


'''To create multidimensional array'''

arr = np.array([1,2,3,4,5] , ndmin=5)

print("Number of dimensions :", arr.ndim)
print(arr)