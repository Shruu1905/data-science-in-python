import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



'''pandas used'''
df = pd.read_csv("project 1\Marathi_Movies_Dataset - Sheet1.csv")



'''Displays frequencies'''
print("Dataset shape:", df.shape)
print(df.head())



'''matplot and seaborn used'''
'''a bargraph of imdb rating and their frequencies'''
sns.histplot(df['imdb_rating'], bins=10, kde=True)
plt.title("IMDb Rating Distribution (Marathi Movies)")
plt.xlabel('IMdb Rating')
plt.ylabel('Frequency')
plt.show()



'''Display the no.of genres and their frequencies'''
print(df['genre'].value_counts())



'''A horizontal bargraph of rating based on genre'''
genre_rating = df.groupby('genre')['imdb_rating'].mean().sort_values()

genre_rating.plot(kind='barh', figsize=(8,5))
plt.title("Average IMDb Rating by Genre")
plt.xlabel("IMDb Rating")
plt.show()
