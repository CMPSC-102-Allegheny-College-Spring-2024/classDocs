#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Application 5: Movie Recommendation System using Sets")

# User movie preferences
user1_movies = {'The Matrix', 'Inception', 'Interstellar', 'The Dark Knight'}
user2_movies = {'Inception', 'The Dark Knight Rises', 'Pulp Fiction', 'Forrest Gump'}

# Recommend movies based on mutual interest
recommended_movies = user1_movies.intersection(user2_movies)

# Display results
print(f"User 1 Movie Preferences: {user1_movies}")
print(f"User 2 Movie Preferences: {user2_movies}")
print(f"Recommended Movies: {recommended_movies}")
