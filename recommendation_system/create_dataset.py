import pandas as pd
import random
import numpy as np

# Step 1: Define movies and users
movies = [
    {"movie_id": f"movie_{i+1}", "title": title, "genre": genre}
    for i, (title, genre) in enumerate([
        ("The Shawshank Redemption", "Drama"),
        ("The Godfather", "Crime, Drama"),
        ("The Dark Knight", "Action, Crime"),
        ("Inception", "Action, Sci-Fi"),
        ("Forrest Gump", "Drama, Romance"),
        ("Titanic", "Drama, Romance"),
        ("Interstellar", "Sci-Fi, Drama"),
        ("The Matrix", "Action, Sci-Fi"),
        ("Avengers: Endgame", "Action, Adventure"),
        ("The Lion King", "Animation, Family"),
        ("Toy Story", "Animation, Comedy"),
        ("Finding Nemo", "Animation, Family"),
        ("Joker", "Crime, Drama"),
        ("Parasite", "Thriller, Drama"),
        ("The Silence of the Lambs", "Thriller, Horror"),
        ("Schindler's List", "Drama, History"),
        ("Gladiator", "Action, Drama"),
        ("The Social Network", "Biography, Drama"),
        ("Black Panther", "Action, Sci-Fi"),
        ("Frozen", "Animation, Family"),
    ])
]

users = [f"user_{i+1}" for i in range(75)]  # 75 users

# Step 2: Generate random user-movie interactions
def generate_interactions(users, movies, min_ratings=5, max_ratings=20):
    interactions = []
    for user in users:
        # Each user rates a random number of movies
        num_ratings = random.randint(min_ratings, max_ratings)
        rated_movies = random.sample(movies, num_ratings)
        for movie in rated_movies:
            rating = round(random.uniform(1.0, 5.0), 1)  # Ratings between 1.0 and 5.0
            timestamp = pd.Timestamp.now() - pd.to_timedelta(random.randint(0, 365), unit='d')  # Random past date
            interactions.append({
                "user_id": user,
                "movie_id": movie["movie_id"],
                "rating": rating,
                "timestamp": timestamp
            })
    return interactions

interactions = generate_interactions(users, movies)

# Step 3: Save to CSV
interactions_df = pd.DataFrame(interactions)
interactions_df.to_csv("movie_interactions.csv", index=False)

# Movie metadata (optional)
movies_df = pd.DataFrame(movies)
movies_df.to_csv("movies_metadata.csv", index=False)

print("Datasets created: 'movie_interactions.csv' and 'movies_metadata.csv'")
