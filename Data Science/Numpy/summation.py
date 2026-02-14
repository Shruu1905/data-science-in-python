import numpy as np

array = np.array([1,2,3,4,5])

summation_result = np.sum(array)

axis_result = np.sum(array , axis = 0)

cummaltive_result = np.cumsum(array)

print(summation_result)
print(axis_result)
print(cummaltive_result)