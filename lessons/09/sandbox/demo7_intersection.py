#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code to demonstrate intersection. 

# A die can roll prime numbers {2, 3, 5}  or odd numbers {1, 3, 5). What are the chances of a die roll is both prime AND odd? 

# To find the probability of rolling a number on a die that is both prime AND odd on a six-sided die, we need to determine the intersection of the sets of prime numbers and odd numbers. The numbers that satisfy both conditions are {3, 5}. The probability is then calculated as the ratio of the number of successful outcomes to the total possible outcomes. """

from sympy import FiniteSet, Rational

def calculate_probability(successful_outcomes, total_outcomes):
    """ Function to use lengths of sets to determine probability"""
    return Rational(len(successful_outcomes), total_outcomes)
# end of calculate_probability()

# Define the set of prime numbers on the die
prime_numbers = FiniteSet(2, 3, 5)

# Define the set of odd numbers on the die
odd_numbers = FiniteSet(1, 3, 5)

# Find the intersection of prime and odd numbers
prime_and_odd_numbers = prime_numbers.intersect(odd_numbers)

# Total number of possible outcomes on a six-sided die
total_possible_outcomes = 6

# Calculate and display the probability of rolling a number that is both prime and odd
probability_prime_and_odd = calculate_probability(prime_and_odd_numbers, total_possible_outcomes)
print(f"Probability of rolling a number that is both prime and odd: {probability_prime_and_odd}")

