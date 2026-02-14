import numpy as np

array = np.array([1,2,3,4,5])

product_result = np.prod(array)

axis_product_result = np.prod(array , axis = 0)

cummalative_product_array = np.cumprod(array)

print(product_result)
print(axis_product_result)
print(cummalative_product_array)