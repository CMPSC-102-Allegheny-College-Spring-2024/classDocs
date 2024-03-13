#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This example defines a six-sided die using FiniteSet and calculates the probability of getting an even number or a number greater than 4. The calculate_probability function is used to compute the probability of an event based on the number of favorable outcomes and the total number of possible outcomes. The Rational class from sympy is used to represent exact fractions to maintain precision in the probability calculations.


from sympy import FiniteSet, Rational


def calculate_probability(outcomes, total_outcomes):
    """ Function to use lengths of sets to determine probability"""
    return Rational(len(outcomes), total_outcomes) # return a fraction
# end of calculate_probability()

# Define a six-sided die
die_outcomes = FiniteSet(1, 2, 3, 4, 5, 6)

# Choose an event, for example, getting an even number
even_numbers = FiniteSet(2, 4, 6)

# Calculate and display the probability of getting an even number
probability_even_numbers = calculate_probability(even_numbers, len(die_outcomes))
print(f"Probability of getting an even number: {probability_even_numbers}")

# Choose another event, for example, getting a number greater than 4
numbers_greater_than_4 = FiniteSet(5, 6)

# Calculate and display the probability of getting a number greater than 4
probability_greater_than_4 = calculate_probability(numbers_greater_than_4, len(die_outcomes))
print(f"Probability of getting a number greater than 4: {probability_greater_than_4}")

