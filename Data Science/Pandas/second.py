'''To read/print data from a csv file'''
'''pd.read_csv() to read the data '''

import pandas as pd


file_path = 'Data Sets\Hindi-Marathi_movies.csv'
df = pd.read_csv(file_path)


'''to display data in specific range'''
pd.options.display.max_rows = 999

print(df)



'''To read/print data from a json file'''
'''pd.read_json() to read the data '''

file_name = 'Data Sets/intents.json'
df = pd.read_json(file_name)
print(df)