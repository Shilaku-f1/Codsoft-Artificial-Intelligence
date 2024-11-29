import pandas as pd
from flask import Flask, render_template, request
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the datasets
movies_df = pd.read_csv('movies_metadata.csv')

# Load the Collaborative Filtering model (if saved)
# If you used SVD, you can pickle it and load it here
# with open('collaborative_filtering_model.pkl', 'rb') as f:
#     collaborative_model = pickle.load(f)

# Load the Content-Based Filtering model (genre-based)
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['genre'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get recommendations based on movie title
def get_content_based_recommendations(movie_title):
    idx = movies_df.index[movies_df['title'] == movie_title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return movies_df['title'].iloc[movie_indices]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.form['movie_title']
    recommendations = get_content_based_recommendations(movie_title)
    return render_template('index.html', movie_title=movie_title, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
