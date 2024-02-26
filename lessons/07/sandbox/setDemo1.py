#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Application 1: Common Interests in Social Networks")

# Define users and their interests
user1_interests = {'music', 'sports', 'travel'}
user2_interests = {'sports', 'reading', 'movies'}
user3_interests = {'travel', 'photography', 'music'}

# Find common interests
common_interests = user1_interests.intersection(user2_interests, user3_interests)

# Display results
print(f"User 1 Interests: {user1_interests}")
print(f"User 2 Interests: {user2_interests}")
print(f"User 3 Interests: {user3_interests}")
print(f"Common Interests: {common_interests}")
