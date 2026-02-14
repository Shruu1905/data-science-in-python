import matplotlib.pyplot as plt

x = [2,3,4,5,6]
y = [10,20,15,20,30]

plt.scatter(x,y , color='red' , marker='*' , s=300 , edgecolors='black')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.title('Customized Scatter plot')
plt.show()