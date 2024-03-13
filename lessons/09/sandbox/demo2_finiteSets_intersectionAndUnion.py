#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code to demonstrate how to fine the union and intersection of finite sets.

from sympy import FiniteSet

# Create finite sets using FiniteSet
set1 = FiniteSet(1, 2, 3, 4, 5)
set2 = FiniteSet(3, 4, 5, 6, 7)

# Display sets
print("Set 1:", set1)
print("Set 2:", set2)

# Union of sets
union_set = set1.union(set2)
print("Union of Set 1 and Set 2:", union_set)

# Intersection of sets
intersection_set = set1.intersect(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# Check if an element is in a set
element_to_check = 3
is_element_in_set1 = element_to_check in set1
is_element_in_set2 = element_to_check in set2

print(f"Is {element_to_check} in Set 1?", is_element_in_set1)
print(f"Is {element_to_check} in Set 2?", is_element_in_set2)
