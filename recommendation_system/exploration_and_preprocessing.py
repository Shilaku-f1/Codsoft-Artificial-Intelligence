import pandas as pd
import os
from sklearn.model_selection import train_test_split  # Add this import

# Step 1: Load the datasets
interactions_df = pd.read_csv("movie_interactions.csv")
movies_df = pd.read_csv("movies_metadata.csv")

# Step 2: Inspect the datasets (optional)
print("Interactions Dataset:")
print(interactions_df.head())
print("\nMovies Metadata Dataset:")
print(movies_df.head())

# Step 3: Data Exploration
# Number of unique users and movies
num_users = interactions_df['user_id'].nunique()
num_movies = interactions_df['movie_id'].nunique()
print(f"\nNumber of Users: {num_users}")
print(f"Number of Movies: {num_movies}")

# Average rating per movie
avg_ratings = interactions_df.groupby('movie_id')['rating'].mean()
print(f"\nAverage Ratings (Top 5):\n{avg_ratings.head()}")

# Step 4: Data Preprocessing
# Encode user_id and movie_id to numeric values
interactions_df['user_id'] = interactions_df['user_id'].astype('category').cat.codes
interactions_df['movie_id'] = interactions_df['movie_id'].astype('category').cat.codes

# Split the dataset into training and testing sets (80-20 split)
train_data, test_data = train_test_split(interactions_df, test_size=0.2, random_state=42)

# Save processed datasets
train_file = "train_data.csv"
test_file = "test_data.csv"
train_data.to_csv(train_file, index=False)
test_data.to_csv(test_file, index=False)

# Confirm file creation
if os.path.exists(train_file) and os.path.exists(test_file):
    print(f"Datasets successfully created: '{train_file}' and '{test_file}'")
else:
    print("Error: Datasets not found!")

# Optionally, print some sample data from the files
print(f"\nSample from {train_file}:")
print(train_data.head())
