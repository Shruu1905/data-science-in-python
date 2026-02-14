'''np.random.binomial()'''
import numpy as np
import matplotlib.pyplot as plt

n , p , size = 10 , 0.5 , 1000

data = np.random.binomial(n , p ,size)

count , bins , ignored = plt.hist(data , 11 , density = True)

plt.show()