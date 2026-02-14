'''ufunc : universal function'''
import numpy as np 

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([5,4,3,2,1])

add_result = np.add(arr1 , arr2)
subtract_result = np.subtract(arr1 , arr2)

print(add_result)
print(subtract_result)