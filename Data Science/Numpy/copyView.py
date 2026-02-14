'''The number in the particular index number is replaced by another number , rest of the array is copied as it is
          USING COPY() FUNCTION AND VIEW() FUNCTION  '''
import numpy as np

og_array = np.array([0,1,2,3,4,5])

copied_array = og_array.copy()
copied_array[0] = 7

array_view = og_array.view()
array_view[0] = 19

print("Og array : " , og_array)

print("Copied Array :" , copied_array)

print("Copied Array :" , array_view)