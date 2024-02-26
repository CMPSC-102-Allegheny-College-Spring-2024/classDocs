#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Application 3: Word Frequency Counter in a Text")

# Simulate a text
text = "This is a sample text. It contains some words, and some words may repeat."

# Split the text into words
words = text.lower().split()

# Use a set to get unique words
unique_words = set(words)

# Count word frequencies
word_frequencies = {word: words.count(word) for word in unique_words}

# Display results
print(f"Original Text: {text}")
print(f"Word Frequencies: {word_frequencies}")

