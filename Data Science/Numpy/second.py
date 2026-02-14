'''To choose a random number from a range '''
'''1)randint(range): is the function to select random integer
   2)rand(): is the function to select random decimal number
   3)randint (range , size = (number)) : to make 1D array of random numbers  
   4)randint (range , size = (number of rows , number of elements)) : to make 2D array of random numbers 
   5).choice([array]) : to select random number from a given array
   6).choice([array , size ()]) : to create 2D from a given array of the given size
'''

from numpy import random

x = random.randint(200)

print(x)


y = random.rand()
print(y)

z = random.randint(200 , size = (5))
print(z)

a = random.randint(200 , size = (4 , 5))
print(a)

b = random.choice([20 , 7 , 9 , 435 , 68])
print(b)

c = random.choice([2 , 88 , 12 , 45 , 61 , 35 , 22 , 77] , size = (4,2))
print(c)