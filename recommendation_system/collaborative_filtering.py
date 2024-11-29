import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import mean_squared_error
import numpy as np

# Step 1: Load the train dataset
train_data = pd.read_csv("train_data.csv")

# Step 2: Create a user-item matrix
user_item_matrix = train_data.pivot_table(index='user_id', columns='movie_id', values='rating')

# Step 3: Apply Singular Value Decomposition (SVD)
svd = TruncatedSVD(n_components=10, random_state=42)
user_item_matrix_svd = svd.fit_transform(user_item_matrix.fillna(0))  # Fill NaN values with 0

# Step 4: Reconstruct the matrix using SVD results
reconstructed_matrix = np.dot(user_item_matrix_svd, svd.components_)

# Step 5: Compute Mean Squared Error (MSE) to evaluate the model
# First, we need to reshape the reconstructed matrix to match the user-item matrix shape
reconstructed_matrix_df = pd.DataFrame(reconstructed_matrix, columns=user_item_matrix.columns, index=user_item_matrix.index)

# Calculate the mean squared error between the actual and reconstructed ratings
mse = mean_squared_error(user_item_matrix.fillna(0), reconstructed_matrix_df.fillna(0))
print(f"Mean Squared Error: {mse}")

# Step 6: Predict ratings for a specific user (e.g., user_1)
user_id = 1  # For example, user_1
user_ratings = reconstructed_matrix_df.loc[user_id]
predicted_ratings = user_ratings.sort_values(ascending=False)

# Show top 5 movie recommendations for user_1
top_5_recommendations = predicted_ratings.head(5)
print("\nTop 5 Movie Recommendations for user_1:")
print(top_5_recommendations)
