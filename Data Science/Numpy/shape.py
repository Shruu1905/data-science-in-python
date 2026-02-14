'''shape method describes the size , rows and columns of the arrays/matrix'''
import numpy as np

array_1d = np.array([1,2,3,4,5])

array_2d = np.array([[1,2,3] , 
                     [4,5,6]])


array_3d = np.array([[[1,2,3] , 
                      [4,5,6], 
                      [7,8,9]] ])

print(array_1d.shape)

print(array_2d.shape)

print(array_3d.shape)


