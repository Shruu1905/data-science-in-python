import pandas as pd


df = pd.read_csv('Data Sets/data.csv')
print(df.head()) ;                 '''df.head(n)  =   to print first n no. of rows
                                      df.head()  =   to print only 1st 5 rows''' 



print(df.tail(10)) ;                 '''df.tail(n)  =   to print last n no. of rows
                                      df.tail()  =   to print only last 5 rows''' 




'''df.info()   =    to print info of csv file'''
print(df.info())