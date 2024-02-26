#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

print("Application 10: Calculation of Sin Using the Taylor Series")

def calculate_sin_taylor_series(x, terms=10):
    """ Use the Taylor series to approximate sin value """
    result = 0
    for n in range(terms):
        # sin(x) = x - (x^3 / 3!) + (x^5 / 5!) - ...
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        result += term
    return result
# end of calculate_sin_taylor_series()

def main(value:int) -> None:
    """ Driver function """

    # Test the function
    angle_in_radians = math.radians(value)  # Convert angle to radians
    sin_approximation = calculate_sin_taylor_series(angle_in_radians, terms=10)

    angleInRad = round(math.degrees(angle_in_radians),2)
    actualSinVal = math.sin(angle_in_radians)

    print(f"Approximation of sin({angleInRad} degrees): {sin_approximation}")
    print(f"Actual sin({angleInRad} degrees): {actualSinVal}")
    print(f"Error: {abs(actualSinVal - sin_approximation)}")
# end of main()

for i in range(400):
    main(i)
    print("\t -----")