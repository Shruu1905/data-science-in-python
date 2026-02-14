import numpy as np

decimal_array = np.array([3.234456 , 5.24333532 , 52.45982 , 842.4321117])

rounded_array = np.round(decimal_array , decimals=3)
print(rounded_array)

around_array = np.around(decimal_array , decimals=2)
print(around_array)