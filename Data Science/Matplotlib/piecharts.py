import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,30,10])
mylabels = ['A' , 'B' , 'C' , 'D']

plt.pie(y , labels=mylabels)
plt.show()



'''To start the sections from a specific angle'''
'''To add a legend'''
x = np.array([35,25,30,10])
mylabels = ['A' , 'B' , 'C' , 'D']
plt.pie(x , labels=mylabels , startangle=90)
plt.legend()
plt.show()