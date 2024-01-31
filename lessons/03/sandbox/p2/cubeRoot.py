#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def cube_root_approximation(number, tolerance=1e-6):
    # Initial guess for the cube root
    # guess = number / 2.0 # one way to start
    guess = 5
    # Iterate until the approximation is within the specified tolerance
    while abs(guess**3 - number) > tolerance:
        # Update the guess using the approximation formula
        guess = (2 * guess + number / (guess**2)) / 3.0
        print(f" guess = {guess}")

    return guess

# Example: Calculate the cube root of 29791
input_number = 29791
result = cube_root_approximation(input_number)

# Display the result
print(f"The cube root of {input_number}")
print(f" is approximately: {result}")
