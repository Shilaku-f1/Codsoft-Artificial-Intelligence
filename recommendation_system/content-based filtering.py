import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load the datasets
movies_df = pd.read_csv("movies_metadata.csv")

# Step 2: Vectorize the movie genres using TF-IDF
# We'll use a TfidfVectorizer to convert the 'genre' column into a matrix of TF-IDF features
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['genre'])

# Step 3: Compute the cosine similarity between the movies
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Step 4: Create a function to get movie recommendations based on a movie's title
def get_recommendations(movie_title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = movies_df.index[movies_df['title'] == movie_title].tolist()[0]
    
    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the scores of the 5 most similar movies (excluding the movie itself)
    sim_scores = sim_scores[1:6]
    
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    
    # Return the top 5 most similar movies
    return movies_df['title'].iloc[movie_indices]

# Step 5: Test the recommendations
movie_title = "The Shawshank Redemption"  # Example movie
recommendations = get_recommendations(movie_title)
print(f"\nTop 5 Content-Based Recommendations for '{movie_title}':")
print(recommendations)
