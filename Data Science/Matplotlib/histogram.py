'''plt.hist =  to create a histogram'''
import matplotlib.pyplot as plt
import numpy as np                          ; '''For 2nd plot'''

data = [2,3,4,2,4,3,3,3,2,5,6,5,6,4 ]

plt.hist(data , bins=5 , color='red' , edgecolor='black')
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()



x = np.random.normal(170 , 10 , 250)
plt.hist(x)
plt.show()