'''Using numpy'''
from numpy import random  


'''Using matplot for visualization'''
import matplotlib.pyplot as plt
import seaborn as sns

'''Normal distribtion is created using random.normal'''
'''loc means mean    and    scale means standard deviation'''
x = random.normal(size=[2,3])
y = random.normal(loc = 1 , scale= 2 , size=[2,3])
print(x)
print(y)

sns.distplot(random.normal(size=100) , hist=False)
plt.show()
