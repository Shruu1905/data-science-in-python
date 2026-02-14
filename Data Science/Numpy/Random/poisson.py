'''random.poisson()'''
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.poisson(lam=2 , size=10)
print(x)

sns.distplot(random.poisson(lam=2 , size=10) , kde=False )
plt.show()