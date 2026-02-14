'''random is included in numpy'''

from numpy import random

'''1d array'''
x = random.choice([1,2,3,4] , p=[0.1 , 0.2 , 0.3 , 0.4] ,  size= (10))

'''2d array'''
y = random.choice([1,2,3,4] , p=[0.1 , 0.2 , 0.3 , 0.4] ,  size= (2,3))
print(x)

print(y)