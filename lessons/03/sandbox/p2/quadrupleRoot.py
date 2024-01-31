#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def quadruple_root_approximation(number, tolerance=1e-6):
    # Initial guess for the fourth root
    guess = number / 2.0

    # Iterate until the approximation is within the specified tolerance
    while abs(guess**4 - number) > tolerance:
        # Update the guess using the approximation formula
        guess = (3 * guess + number / (guess**3)) / 4.0
        print(f" guess = {guess}")

    return guess

# Example: Calculate the fourth root of 2401
input_number = 2401
result = quadruple_root_approximation(input_number)

# Display the result
print(f"The fourth root of {input_number}")
print(f" is approximately: {result}")