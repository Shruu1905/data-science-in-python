'''random.shuffle is used to shuffle the poition of numbers in the array'''
'''for 2d array rows and columns are premutated'''
import numpy as np 

og_array = np.array([1,2,3,4,5])

shuffled_array = np.random.shuffle(og_array)
premutated_array = np.random.permutation(og_array)

print('shuffled array : ', shuffled_array)
print('premutated array : ', premutated_array)