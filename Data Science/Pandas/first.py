'''COLUMNAR DATA - SPREADSHEET'''

import pandas as pd

'''Series with custom index'''
a = [1,2,3]
myVar1 = pd.Series(a , index=["p" , "q" , "r"])

print(myVar1)




'''Series from list'''

data_list = [1,2,3,4,5]

series_from_list = pd.Series(data_list)

print("Series from list : " , series_from_list)




'''Data from index'''

data = {'a' : 10 , 'b': 20 , 'c': 30 , 'd':40}

data_dict = pd.Series(data)

print(data_dict)




'''pd.DataFrame to make a data frame'''
'''Data Frame - 2D'''
'''Eg of data from dict'''
myDataSet = {
    'Name' : ["Shruti" , "Adit" , "John" , "Doe"] ,
    'Marks' : [90 , 85 , 80 , 88] ,
    'city' : ['Mumbai' , 'Thane' , 'Pune', 'Banglore']
}

myVar = pd.DataFrame(myDataSet) 

print(myVar)



'''Eg of data from list'''
myData = [{'name' : 'David' , 'age' : 25 , 'City' : 'New Delhi'} ,
         {'name' : 'Alex' , 'age' : 30 , 'City' : 'Canada'} ,
         {'name' : 'Ben' , 'age' : 22 , 'City' : 'Sdyeny'} ,
         {'name' : 'Alice' , 'age' : 24 , 'City' : 'Berlin'}]

data_from_list = pd.DataFrame(myData)

print(data_from_list)