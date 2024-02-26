#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Application 8: Inclusion-Exclusion Principle")

# Define sets and their sizes
set_A = {1, 2, 3, 4, 5}
set_B = {3, 4, 5, 6, 7}
set_C = {5, 6, 7, 8, 9}

# Inclusion-Exclusion Principle
inclusion_exclusion_result = len(set_A.union(set_B, set_C))

# Display results
print(f"Set A: {set_A}")
print(f"Set B: {set_B}")
print(f"Set C: {set_C}")
print(f"Size of Union (Inclusion-Exclusion): {inclusion_exclusion_result}")
9