#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity

# Movies dataset
movies = {
    'MovieID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Movie Title': [
        'The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 
        'Pulp Fiction', 'Inception', 'Forrest Gump', 'The Matrix', 'Interstellar'
    ]
}
movies_df = pd.DataFrame(movies)

# Ratings dataset
ratings = {
    'UserID': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
    'MovieID': [1, 2, 3, 1, 2, 4, 3, 5, 6, 4, 7, 8],
    'Rating': [5, 4, 3, 4, 5, 3, 5, 4, 3, 5, 4, 3]
}
ratings_df = pd.DataFrame(ratings)

# Create a user-movie rating matrix
user_movie_matrix = ratings_df.pivot(index='UserID', columns='MovieID', values='Rating').fillna(0)
print("User-Movie Rating Matrix:")
print(user_movie_matrix)

# Calculate cosine similarity between movies
cosine_sim = cosine_similarity(user_movie_matrix.T)  # Transpose to get movie-movie similarity
cosine_sim_df = pd.DataFrame(cosine_sim, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)
print("\nCosine Similarity Matrix (Movie-Movie):")
print(cosine_sim_df)

def recommend_movies(user_id, num_recommendations=5):
    # Get movies not rated by the user
    user_ratings = user_movie_matrix.loc[user_id]
    unrated_movies = user_ratings[user_ratings == 0].index

    # Predict ratings for unrated movies
    predicted_ratings = {}
    for movie_id in unrated_movies:
        # Find similar movies
        similar_movies = cosine_sim_df[movie_id].sort_values(ascending=False)
        # Get ratings of the user for similar movies
        similar_movies_rated = similar_movies[user_ratings[similar_movies.index] > 0]
        # Predict rating as the weighted average of similar movies' ratings
        predicted_rating = np.dot(similar_movies_rated, user_ratings[similar_movies_rated.index]) / similar_movies_rated.sum()
        predicted_ratings[movie_id] = predicted_rating

    # Sort predicted ratings and get top recommendations
    recommended_movies = sorted(predicted_ratings.items(), key=lambda x: x[1], reverse=True)[:num_recommendations]
    return recommended_movies

# Function to display recommended movies
def display_recommendations(user_id, recommendations):
    print(f"\nTop Recommendations for User {user_id}:")
    for movie_id, predicted_rating in recommendations:
        movie_title = movies_df[movies_df['MovieID'] == movie_id]['Movie Title'].values[0]
        print(f"{movie_title} (Predicted Rating: {predicted_rating:.2f})")
        
        # Example: Recommend movies for User 1
user_id = 1
recommendations = recommend_movies(user_id)
display_recommendations(user_id, recommendations)


# In[ ]:




