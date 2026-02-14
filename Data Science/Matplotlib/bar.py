import matplotlib.pyplot as plt

categories = ['Catergory A' , 'Catergory B' , 'Catergory C' , 'Catergory D']
values = [30,40,20,25]


plt.bar(categories , values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Vertical Bar Plot')

plt.show()


'''plt.barh()  =   to create horizontal bar graphs/plots '''
plt.barh(categories , values , color=['blue' , 'red' , 'orange' , 'yellow'])
plt.ylabel('Categories')
plt.xlabel('Values')
plt.title('Horizontal Bar Plot')

plt.show()