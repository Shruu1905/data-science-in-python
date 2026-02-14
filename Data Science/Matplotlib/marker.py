import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,30,20,10,30]


plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Types of markers')
plt.legend()


'''types of markers'''
plt.plot(x ,y , marker='o' , label='Circle')
plt.show()
plt.plot(x ,y , marker='s' , label='Square')
plt.show()
plt.plot(x ,y , marker='^' , label='Triangle')
plt.show()
plt.plot(x ,y , marker='*' , label='Star')
plt.show()


plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Types of markers')
plt.legend()

