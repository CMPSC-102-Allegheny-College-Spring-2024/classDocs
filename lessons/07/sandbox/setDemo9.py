#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Application 9: Power Set Calculation")

def calculate_power_set(original_set):
    power_set = [set()]
    for element in original_set:
        new_subsets = [subset.union({element}) for subset in power_set]
        power_set.extend(new_subsets)
    return power_set

# Define a set
original_set = {1, 2, 3}

# Calculate and display the power set
power_set_result = calculate_power_set(original_set)
print(f"Original Set: {original_set}")
print(f"Power Set: {power_set_result}")
