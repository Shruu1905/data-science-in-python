'''Reshaping the array shape'''
import numpy as np

og_array = np.array([1,2,3,4,5,6])

reshaped_array = og_array.reshape(2,3)

row_major = og_array.reshape(2,3 , order="C")
column_major = og_array.reshape(2,3 , order="F")


print(og_array)
print(reshaped_array)
print(row_major)
print(column_major)
