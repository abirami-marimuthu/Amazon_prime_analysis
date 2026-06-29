import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('amazon_prime.csv')
print(df.head())

print(df.info())
print(df.shape)
print(df.columns)


print(df.isnull().sum())

print(df['IMDb_Rating'].describe())

"TOP 10 GENRES"
genre_count = df["Genre"].value_counts()
print(genre_count.head(10))

"TOP LANGUAGES"
language_count = df["Language"].value_counts()
print(language_count)

# Highest Rated Shows
top_rated = df.sort_values(
    by="IMDb_Rating",
    ascending=False
)

print("\nTop Rated Shows:")
print(top_rated[["Show_Name", "IMDb_Rating"]].head(10))

#SHOWS RELEASED EACH YEAR
year_count=df.groupby('Release_Year').size()
print("\nShows Released Each Year:")
print(year_count)


#BAR CHART OF TOP 10 GENRES
import matplotlib.pyplot as plt
genre_count.head(10).plot(kind='bar')
plt.title('Top 10 Genres on Amazon Prime') 
plt.xlabel('Genre')
plt.ylabel('Number of Shows')
plt.show()

#LANGUAGE CHART
language_count.head(10).plot(kind='bar')
plt.title('Top Languages on Amazon Prime')
plt.xlabel('Language')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.show()

print(genre_count.head(10))

#RELEASE TREND CHART
year_count.plot(kind='line')
plt.title('Release Trend on Amazon Prime')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('release_trend.png')  # Save the plot as an image file
plt.show()

#IMDB RATING DISTRIBUTION

df['IMDb_Rating'].plot(kind='hist', bins=20)
plt.title('IMDb Rating Distribution')
plt.xlabel('IMDb Rating')
plt.tight_layout()
plt.savefig('imdb_rating_distribution.png')  # Save the plot as an image file
plt.show()