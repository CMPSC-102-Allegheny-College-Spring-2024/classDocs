#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Application 7: Set Operations with Mathematical Equations")

# Define sets
set_A = {1, 2, 3, 4, 5}
set_B = {3, 4, 5, 6, 7}

# Mathematical operations on sets
union_result = set_A.union(set_B)
intersection_result = set_A.intersection(set_B)
difference_result = set_A - set_B
symmetric_difference_result = set_A.symmetric_difference(set_B)

# Display results
print(f"Set A: {set_A}")
print(f"Set B: {set_B}")
print(f"Union: {union_result}")
print(f"Intersection: {intersection_result}")
print(f"Difference (A - B): {difference_result}")
print(f"Symmetric Difference: {symmetric_difference_result}")