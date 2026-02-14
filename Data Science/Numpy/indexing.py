'''To create a array and display the element using the index number'''
'''In multidimensional the arrays as 
0th row   : 0th element   1st element   2nd element  ........     nth element
1st row
2nd row 
.....
nth row '''


import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr[2])

print(arr[-1])

'''Boolean Indexing'''
mask = arr >  2
print(arr[mask])

arr_2D = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
print(arr_2D)
print(arr_2D[1,2])

