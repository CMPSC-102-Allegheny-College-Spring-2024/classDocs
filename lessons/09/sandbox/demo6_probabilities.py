#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This example defines a standard deck of playing cards, creates a set of all possible cards, and calculates the probability of drawing a face card or a red card from the deck. The calculate_probability function is used to compute the probability based on the number of favorable outcomes and the total number of possible outcomes.

from sympy import FiniteSet, Rational

def calculate_probability(outcomes, total_outcomes):
    """ Function to use lengths of sets to determine probability"""
    return Rational(len(outcomes), total_outcomes)
# end of calculate_probability()

# Define a standard deck of playing cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Create a set of all possible cards in the deck
deck = FiniteSet(*[(rank, suit) for rank in ranks for suit in suits])
print(f" My deck is the following : {deck}\n")

# Choose an event, for example, drawing a face card
face_cards = FiniteSet(*[(rank, suit) for rank in ['Jack', 'Queen', 'King'] for suit in suits])

# Calculate and display the probability of drawing a face card
probability_face_card = calculate_probability(face_cards, len(deck))
print(f"Probability of drawing a face card: {probability_face_card}")

# Choose another event, for example, drawing a red card
red_cards = FiniteSet(*[(rank, suit) for rank in ranks for suit in suits if suit in ['Hearts', 'Diamonds']])

# Calculate and display the probability of drawing a red card
probability_red_card = calculate_probability(red_cards, len(deck))
print(f"Probability of drawing a red card: {probability_red_card}")
