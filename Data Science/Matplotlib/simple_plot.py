import matplotlib.pyplot as plt 

x = [1,2,3,4,5]           ; '''these arrays can be made using numpy also but to use it first import numpy and np.array[(array elements)]'''
y = [10,20,30,30,10]
x2 = [5,4,3,2,1]
y2 = [20,10,0,-10,30]

plt.plot(x , y) ;  '''plt.plot()   =   to plot x and y in same graph '''
plt.show()      ;  '''plt.show()   =   to plot the graph'''




'''Customization of plotting'''
plt.plot(x , y , marker='o' , linestyle='--' , color='red', label='Dashed Red Line')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Customization Line Stye and Color')
plt.legend()
plt.show()


plt.plot(x,y, 'o') ;              '''to plot without graph'''
plt.show()


'''Adding grid and customizing'''
'''Mutiple lines on single plot'''
plt.plot(x,y , label='Line 1')
plt.plot(x2 ,y2 , label='Line 2' , linestyle='--' ,  color='green')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Multiple lines on single plot')
plt.legend(loc='upper left' , fontsize=12 , frameon=False) ;           '''Customization of legend'''
plt.grid(color='red' , linestyle='--' , linewidth=0.5)
plt.show()