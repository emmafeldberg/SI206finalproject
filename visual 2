import matplotlib.pyplot as plt

# JSON data containing information about movies
movies_data = [
    {"title": "Deadpool", "year": 2016},
    {"title": "Guardians of the Galaxy", "year": 2014},
    {"title": "The Dark Knight", "year": 2008},
    {"title": "Interstellar", "year": 2014},
    {"title": "Inception", "year": 2010},
    {"title": "The Avengers", "year": 2012},
    {"title": "Doctor Strange", "year": 2016},
    {"title": "The Matrix", "year": 1999},
    {"title": "Logan", "year": 2017},
    {"title": "Avatar", "year": 2009}
]

def count_movies_per_year(movies_data):
    movie_counts = {}
    for movie in movies_data:
        year = movie["year"]
        movie_counts[year] = movie_counts.get(year, 0) + 1
    return movie_counts

def plot_movies_per_year(movie_counts):
    years = list(movie_counts.keys())
    movie_counts_values = list(movie_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(years, movie_counts_values, color='skyblue')
    plt.title('Number of Movies Released Each Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(years)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Count movies per year
movie_counts = count_movies_per_year(movies_data)

# Plot movies per year
plot_movies_per_year(movie_counts)
